import csv
from datetime import datetime
from github import Github
from termcolor import colored

class OutdatedRepos:
    def __init__(self):
        self.g = Github("API_KEY_HERE")
        self.org = self.g.get_organization("ORGANISATION_NAME_HERE")
        self.repos = self.org.get_repos()
        self.current_date = datetime.now()
        self.outdated_repos = []

    def get_repo_data(self):
        for repo in self.repos:
            repo_details = {}
            last_pushed = repo.pushed_at
            last_pushed_str = last_pushed.strftime("%Y-%m-%dT%H:%M:%SZ")
            time_since_last_push = (self.current_date - last_pushed).days
            years, remainder = divmod(time_since_last_push, 365)
            months, days = divmod(remainder, 30)

            if time_since_last_push >= 730:
                repo_details["Name"] = repo.full_name
                repo_details["Desc"] = repo.description
                repo_details["Language"] = ",".join(repo.get_languages().keys())
                repo_details["Last_Push_date"] = last_pushed_str
                repo_details["Years"] = years
                repo_details["Months"] = months
                repo_details["Days"] = days
                
                self.outdated_repos.append(repo_details)

                print(colored(f"[+] {repo.full_name}: Last Push Was --> [ {years} years, {months} months, and {days} days ago {repo_details['Language']} ]", 'yellow'
                ))
        print(colored(f"\n\n[++] A Total of {len(self.outdated_repos)} repos had their last push at least 2 year ago to date {self.current_date} [++]", 'red'
        ))

    def save_as_csv(self):
        with open("inactive_repos.csv", mode="w", newline="") as file:
            fieldnames = [
                "Name",
                "Desc",
                "Language",
                "Last_Push_date",
                "Years",
                "Months",
                "Days",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for repo in self.outdated_repos:
                writer.writerow(repo)
        print(colored(
            f"\n\n[+++] Finished writing results to CSV file > outdated_repos.csv [+++]", 'green'
        ))

    if __name__ == "__main__":

        def main(self):
            self.get_repo_data()
            self.save_as_csv()


reposcan = OutdatedRepos()
reposcan.main()
