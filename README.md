# DevOps Tools Analyzer

## Overview
DevOps Tools Analyzer is a comprehensive tool designed to streamline the management of various DevOps tools, providing insights and analytics across different platforms. This repository features three main menus as of now : Cloud Tools, Ticketing Tools, and SCM Tools.
## Features

### Cloud Tools
Under this, there is support for AWS Cloud Provider.

#### AWS Cloud:
- This contains a submenu containing account names from the Admin Page that stores access & secret key for analysis
- The 360 Page of an AWS account displays information including:
  - Total number of Groups in IAM
  - Total number of Empty groups in IAM
  - Hosted Zones Count in Route53
  - Total Domains Count in Route53
  - Previous and Present Month Cost
- From Hosted Zone info, one can navigate to its details and their records details

### Ticketing Tools
Under this, there is support for Atlassain Jira

#### Atlassian Jira:
- This contains a submenu containing account names from the Admin Page that stores Atlassain URL, Email ID & API Token
- Provides Jira account statistics such as:
   - Number of Business Projects
   - Number of Software Projects
   - Number of Team Managed Projects
   - Company Managed Projects
   - Total Webhooks count
   - Disabled Webhooks Count

### SCM Tools
Under this, there is support for Github

#### GitHub:
- This contains a submenu containing account names from the Admin Page that stores Github Org and API token for it
- Shows GitHub Org details such as:
  - Teams Count
  - Members Count
  - Public Repositories Count
  - Private Repositories Count

## Getting Started
To get started with the DevOps Tools Analyzer, follow these steps:
- Clone the Repository:
```
git clone https://github.com/techiescamp/devops-tools.git
```
- Install Dependencies requests,whitenoise, pygithub, jira, django
- Run the Django Project
- Navigate to the Admin Page to add your account credentials for AWS, Jira, and GitHub.
- Ensure that you have the necessary permissions for the credentails to access these tools.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss changes or improvements.

## License
This project is licensed under the GPL-3.0 license - see the LICENSE file for details.

## Contact
For any inquiries or support, please reach out via the issues section of the repository.
