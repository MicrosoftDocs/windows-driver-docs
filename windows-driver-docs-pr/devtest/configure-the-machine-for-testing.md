#Configure the Machine for Testing
The steps required to install WDTF and TAEF, copy the data-driven tests, configure the machine, and run the tests are outlined below.

**Step 1**: Obtain the packages and files from the latest [EWDK] (https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/installing-the-enterprise-wdk) by accepting the licensing terms and saving the EWDK zip file to the machine on which the tests will run.  Unzip the EWDK.

**Step 2**: Install TAEF by navigating to the location of the TAEF MSI and installing the package for the desired architecture:

    cd <unzipped EWDK root>\Program Files\Windows Kits\10\Testing\Runtimes
    msiexec /i "Test Authoring and Execution Framework x64-x64_en-us.msi"

The TAEF MSI installs TAEF to \Program Files\Windows Kits\10\Testing\Runtimes\TAEF.  Add this directory to the system PATH environment variable and restart the command prompt.

Start the TAEF service if it’s not already running and set to Autostart:
    1.	Launch Services: services.msc
    2.	Double click Te.Service
    3.	Set “Startup type” to “Automatic”
    4.	Click “Start” to start the service

**Step 3**: Install WDTF by navigating to the location of the WDTF MSI (same location as the TAEF MSI above) and installing the package for the desired architecture:

    cd <unzipped EWDK root>\Program Files\Windows Kits\10\Testing\Runtimes
    msiexec /i "Windows Driver Testing Framework (WDTF) Runtime Libraries-x64_en-us.msi"

The WDTF MSI installs WDTF to \Program Files\Windows Kits\10\Testing\Runtimes\WDTF.

**Step 4**: Configure the machine for testing:
    1.	Configure the machine to collect full dumps or attach a kernel debugger
    2.	Since the tests can potentially reboot the machine and need to control the sleep cycles, configure the machine to never sleep, never turn off display, and autologon to a test account (netplwiz.exe).  Obviously, autologon should be used with caution.
