# Configure the Machine for Testing
This topic outlines the steps required to install [WDTF](https://docs.microsoft.com/en-us/windows-hardware/drivers/wdtf/) and [TAEF](https://docs.microsoft.com/en-us/windows-hardware/drivers/taef/), copy the data-driven tests, and configure the machine for testing. Note that the following commands must be executed from an elevated/administrator command prompt because WDTF installation installs drivers on the system.

**Step 1**: Obtain the packages and files from the latest [EWDK](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/installing-the-enterprise-wdk) by accepting the licensing terms and saving the EWDK ISO file to the machine on which the tests will run. To mount the ISO, right-click the ISO file and the click **Mount**. When the ISO is mounted, a drive letter is assigned to the mounted ISO.

**Step 2**: Install TAEF by navigating to the location of the TAEF MSI in the mounted ISO and installing the package for the desired architecture. Specify a location and name for the installation log file, **%USERPROFILE%\Desktop\TAEFInstall.log** in this example:

```
    cd <ISO drive>\Program Files\Windows Kits\10\Testing\Runtimes
    msiexec /i "Test Authoring and Execution Framework x64-x64_en-us.msi" /l* "%USERPROFILE%\Desktop\TAEFInstall.log"
```
The TAEF MSI installs TAEF to **%PROGRAMFILES%\Windows Kits\10\Testing\Runtimes\TAEF**.  Add this directory to the system PATH environment variable and restart the elevated command prompt.

If it’s not already running, start the TAEF service and set to **Autostart**:

    1.	Launch Services: services.msc
    2.	Double-click Te.Service
    3.	Set "Startup" type to "Automatic"
    4.	Click Start to start the service

**Step 3**: Install WDTF by navigating to the location of the WDTF MSI (same location as the TAEF MSI above) and installing the package for the desired architecture. Specify a location and name for the installation log file, **%USERPROFILE%\Desktop\WDTFInstall.log** in this example:
```
    cd <ISO drive>\Program Files\Windows Kits\10\Testing\Runtimes
    msiexec /i "Windows Driver Testing Framework (WDTF) Runtime Libraries-x64_en-us.msi" /l* "%USERPROFILE%\Desktop\WDTFInstall.log"
```
The WDTF MSI installs WDTF to **%PROGRAMFILES%\Windows Kits\10\Testing\Runtimes\WDTF**.

**Step 4**: Configure the machine for testing:
    1.	Configure the machine to collect full dumps or attach a kernel debugger.
    2.	Because the tests can potentially reboot the machine and need to control the sleep cycles, configure the machine to never sleep, never turn off display, and autologon to a test account (netplwiz.exe).  Note that autologon should be used with caution.

**Step 5**: Obtain the data-driven test binaries by copying all files from **\<ISO drive>\Program Files\Windows Kits\10\Testing\Tests\Additional Tests\x64\DevFund\DataDriven** to a local folder such as **%USERPROFILE%\Desktop\Tests**. Unmount the ISO.
