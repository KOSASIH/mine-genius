require 'github/discussions'

class Chatbot {
  def self.respond_to_message(repo, message)
    # Get discussion comments
    comments = GitHub::Discussions.get_comments(repo, message)
    # Respond to the message
    GitHub::Discussions.create_comment(repo, message, "Hello! I'm a chatbot.")
  end
}
