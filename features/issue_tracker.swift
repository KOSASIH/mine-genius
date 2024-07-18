import GitHub

class IssueTracker {
  func trackIssue(repo, issue: String) {
    // Create a new issue on GitHub
    let issue = GitHub.Issue(repo, title: issue)
    // Assign the issue to a user
    issue.assign(to: "username")
  }
}
