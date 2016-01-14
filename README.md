# windows-driver-docs-private
Private branch of Windows driver example code and supporting content.

===================
Open Publishing Quick Start
-----------

Start contributing to your repo using the following steps:

1. Clone the repo:
   ```
   git clone https://github.com/Microsoft/windows-driver-docs-private.git
   ```

2. Make your own branch.  For details, see [Team Workflow](https://ppe.msdn.microsoft.com/en-us/wdg-cpub-test/tedhudek/workflow).
3. Edit the Markdown files using your favorite Markdown editor.
3. Commit and push your changes:
   ```
   git add -u
   git commit -m "update doc"
   git push
   ```

4. Wait for a moment and your changes will be automatically published to:

Sandbox:
* Any branch, including live: https://ppe.msdn.microsoft.com/en-us/windows-drivers/develop/visual_studio_driver_development_environment

Production:
* Live branch: https://msdn.microsoft.com/en-us/windows-drivers/develop/visual_studio_driver_development_environment
* Any other branch: https://ppe.msdn.microsoft.com/en-us/windows-drivers/develop/visual_studio_driver_development_environment

> If you don't have the permission to push to this repo, fork it to your own account and use pull request to submit your changes back.

Validation and Preview
----------------------

Before pushing your changes to remote, you can build and preview your doc in local to discover problems early:

1. To validate your changes, run the command `.\.openpublishing.build.ps1` under the root of the repo.
2. To preview your changes:
   * From a command prompt, run `powershell .openpublishing.build.ps1 -parameters:targets=serve` under the root of the repo.
   * From PowerShell, run '.\.openpublishing.build.ps1 -parameters:targets=serve'
   * Open `http://localhost:8080` in your browser.
