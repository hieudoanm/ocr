package cmd

import (
	"os"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "emojis",
	Short: "emojis CLI application (utilities tools)",
	Long: `The emojis CLI application is a comprehensive backend utility belonging to the utilities suite of tools.

Use this root executable to manage configuring, running, and interacting with all emojis-related operations securely and efficiently from your terminal.`,
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}

func init() {
}
