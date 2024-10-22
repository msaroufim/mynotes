import requests
import datetime
import time
from typing import List, Dict, Optional
from dataclasses import dataclass
from operator import attrgetter

@dataclass
class Issue:
    number: int
    title: str
    url: str
    reactions: int
    comments: int
    created_at: datetime.datetime
    
    def engagement_score(self) -> float:
        """Calculate an engagement score based on reactions and comments"""
        return self.reactions + self.comments

class GitHubAPI:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
    def get_rate_limit(self) -> Dict:
        """Check current API rate limit status"""
        response = requests.get('https://api.github.com/rate_limit', headers=self.headers)
        return response.json()['resources']['core']
    
    def wait_for_rate_limit(self):
        """Check rate limit and wait if necessary"""
        rate_limit = self.get_rate_limit()
        if rate_limit['remaining'] < 2:
            reset_time = datetime.datetime.fromtimestamp(rate_limit['reset'])
            sleep_time = (reset_time - datetime.datetime.now()).total_seconds() + 1
            if sleep_time > 0:
                print(f"\nRate limit reached. Waiting {sleep_time:.0f} seconds until {reset_time}...")
                time.sleep(sleep_time)

    def fetch_issues_page(self, page: int = 1) -> Optional[List[Dict]]:
        """Fetch a single page of issues from the PyTorch repository"""
        self.wait_for_rate_limit()
        
        url = 'https://api.github.com/repos/pytorch/pytorch/issues'
        params = {
            'state': 'open',
            'sort': 'created',
            'direction': 'desc',
            'per_page': 100,
            'page': page
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            return None

def get_all_issues(token: str) -> List[Issue]:
    """Fetch all open issues from the repository"""
    github = GitHubAPI(token)
    all_issues = []
    page = 1
    total_processed = 0
    
    print("Starting to fetch all open issues...")
    print("This may take a while due to API rate limits.")
    
    while True:
        issues_data = github.fetch_issues_page(page)
        
        if not issues_data or len(issues_data) == 0:
            break
            
        for issue_data in issues_data:
            # Skip pull requests
            if 'pull_request' in issue_data:
                continue
                
            issue = Issue(
                number=issue_data['number'],
                title=issue_data['title'],
                url=issue_data['html_url'],
                reactions=issue_data['reactions']['total_count'],
                comments=issue_data['comments'],
                created_at=datetime.datetime.strptime(issue_data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            )
            all_issues.append(issue)
        
        total_processed += len(issues_data)
        print(f"\rProcessed {total_processed} items (Page {page})...", end='', flush=True)
        page += 1
    
    print(f"\nFinished processing {total_processed} items across {page-1} pages")
    print(f"Found {len(all_issues)} open issues (excluding pull requests)")
    
    return all_issues

def save_to_file(issues: List[Issue], filename: str = "pytorch_popular_issues.md"):
    """Save the results to a markdown file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Most Popular PyTorch Open Issues\n\n")
        f.write("*Generated on: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC") + "*\n\n")
        f.write("Issues sorted by engagement score (reactions + comments)\n\n")
        
        for i, issue in enumerate(issues, 1):
            f.write(f"## {i}. {issue.title}\n")
            f.write(f"- **URL:** {issue.url}\n")
            f.write(f"- **Engagement Score:** {issue.engagement_score()}\n")
            f.write(f"- **Reactions:** {issue.reactions}\n")
            f.write(f"- **Comments:** {issue.comments}\n")
            f.write(f"- **Created:** {issue.created_at.strftime('%Y-%m-%d')}\n\n")

def main():
    # Replace with your GitHub personal access token
    token = ''
    
    try:
        # Fetch all issues
        all_issues = get_all_issues(token)
        
        # Sort by engagement score
        sorted_issues = sorted(all_issues, key=lambda x: x.engagement_score(), reverse=True)
        
        # Save top 1000 issues to file
        print("\nSaving top 1000 most engaging issues to file...")
        save_to_file(sorted_issues[:1000])
        
        # Print top 20 to console
        print("\nTop 20 Most Popular Open PyTorch Issues:")
        print("-" * 80)
        
        for i, issue in enumerate(sorted_issues[:20], 1):
            print(f"\n{i}. {issue.title}")
            print(f"   URL: {issue.url}")
            print(f"   Engagement Score: {issue.engagement_score()} (Reactions: {issue.reactions}, Comments: {issue.comments})")
            print(f"   Created: {issue.created_at.strftime('%Y-%m-%d')}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
