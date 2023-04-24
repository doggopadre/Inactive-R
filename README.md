<p align="center">
  <img width="150" height="150" src="https://user-images.githubusercontent.com/55149010/178937674-c3b63dc9-f22a-4745-9e38-1362f73144e7.png">
<h1 align="center">Inactive-R</h1>
</p>


Invalid-R is a tool that scans your Github Organisation for repositories that have gone dormant, with their last push activity at least 2 years from the current date.

This tool aims to reduce clutter in your Organisations, giving you the ability to have visibility on inactive repos which you can then take elect to remove, and in turn reduce your Organisation's risk surface area.

You can tweak this tool to scan for a specific timeline i.e "Scan for repos that had last push activity 3 or 4 or 5 years .... and so on ago". 
The default is 2 years ago.


## Requirements <br>
1. Python 3
2. Linux/Windows/MAC OSX
3. GITHUB API KEY with Organisation Admin Permissions.  

## Running the tool 

* Install Python dependencies

```
pip3 install -r requirements.txt 
```


* Configure the GitHub API KEY and the Organisation Name by exporting them as environment variables. 

**Note**: Make sure that the **API KEY has Organisation Admin Permissions**

```
$ export API_KEY = "API_Key_Here"
$ export ORGANIZATION_NAME = "Org_Name_Here"
```
 
 
## Usage

* To run the tool, simply run the following command:

```
python3 inactive-r.py
```

* The tool will run and show you the following response with the total number of inactive repositories:
 
```
[++] A Total of 288 repos had their last push at least 2 year ago to date 2023-04-18 12:58:09.727511 [++]
``` 
 
* It will also at the same time save the output of the scan to a csv file -> **inactive_repos.csv**, containing the repo fullname, Description, Language, time since last push in years, months and days to the current date of running the script:

```
[+++] Finished writing results to CSV file > outdated_repos.csv [+++]
```
## Contributing

* I totally agree that this tool could've been and can be made even more better, by me or anyone else, That said.... Please fell free to tweak this little scriptiee here and create a PR :thumbsup::
