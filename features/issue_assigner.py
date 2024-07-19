import github

class IssueAssigner {
  def assign_issue(repo, issue):
    # Get team members
    team_members = github.getTeamMembers(repo)
    # Assign issue to a team member
    github.assignIssue(repo, issue, team_members[0])
}
