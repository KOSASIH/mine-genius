package main

import (
	"github.com/actions/runner-go"
)

func main() {
	// Create a new workflow
	workflow := runner.NewWorkflow("my-workflow")
	// Add actions to the workflow
	workflow.AddAction("build", "Build the code")
	workflow.AddAction("test", "Run tests")
	// Run the workflow
	workflow.Run()
}
