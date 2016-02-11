
# Installing the WDK 8.1 Build Environment in a Lab

The Windows Driver Kit (WDK) 8.1 provides a feature that enables you to copy components of Visual Studio and the WDK to a new location and then launch the build environment from the command line. From here you can build Windows drivers without having to run the Visual Studio or WDK installation programs.

You might find this feature useful if you need to integrate the WDK with your build process, or if you want to distribute the build process in a lab or test environment.

**Note**  You can only use this feature for building drivers and applications that use C and C++. This feature cannot be used for managed code or Windows Store apps.


1. Download the Visual Studio and WDK and SDK setup files
-------------------------------------------------------------------------------------------------------------------------------

To run the set up script that enables this feature, you need to provide the paths to the Visual Studio and WDK setup files. Be sure to save these files (rather than install them).

1.  Download [Visual Studio Professional 2013](http://go.microsoft.com/fwlink/p/?linkid=316548) or [Visual Studio Ultimate 2013](http://go.microsoft.com/fwlink/p/?linkid=316520). Download the Product Layout (for example, vs\_ultimate\_download.exe ). When you are asked if you want to run or save vs\_ultimate\_download.exe, click **Run** and then select the download option and specify the download path as **C:\\VSSetup** (this makes the later steps easier). Click **Download** to download and install a local copy of the DVD layout on the computer.
2.  Download the standalone [SDK](http://go.microsoft.com/fwlink/p/?linkid=323507). When you are asked if you want to run or save sdksetup.exe, click **Run** and then specify the download location as **C:\\Kits\\SDK**. Click **Next** and follow the instructions to download the standalone SDK.
3.  Download the [WDK 8.1](http://go.microsoft.com/fwlink/p/?linkid=317353). When you are asked if you want to run or save wdksetup.exe, click **Run** and then specify the download location as **C:\\Kits\\WDK**. Click **Next** and follow the instructions to download the WDK. If you have already installed the WDK on the computer, the web installation program will tell you that the features installed on the computer are up-to-date. To download the WDK setup files so that you can deploy the build environment, click **Next** and specify the **C:\\Kits\\WDK** path.

<span id="download_script"></span><span id="DOWNLOAD_SCRIPT"></span>2. Download the BuildLabSupport files
---------------------------------------------------------------------------------------------------------

To be able install the WDK build environment on computers in a lab, you need to first download the build lab support files on your computer.

1.  Download [BuildLabSupportfiles.zip](http://go.microsoft.com/fwlink/p/?linkid=321805).
2.  Extract the contents of the compressed file to your computer. The extracted files include the BuildLabSupport directory and include the setup files and utilities you need.

<span id="install_script"></span><span id="INSTALL_SCRIPT"></span>3. Install the WDK 8.1 build environment
----------------------------------------------------------------------------------------------------------

The build lab support files include the **setup.ps1** PowerShell command file, which extracts the needed Visual Studio and WDK components and copies them to a target directory (folder). You can then copy this directory to another location, from which you can build projects in a Visual Studio command-line interface (CLI) development environment.

-   Open a Command Prompt window with elevated privileges (**Run as administrator**) and go to the directory where you extracted build lab support files. The PowerShell command script **setup.ps1** is in the &lt;*root*&gt;\\BuildLabSupport directory.

    The syntax for the PowerShell command is as follows:

    <span codelanguage="PowerShell"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">PowerShell</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>powershell –executionpolicy bypass –file Setup.ps1 –DeployBuildLab –VSInstallerPath &lt;VSInstallerFilePath&gt; -KitInstallersPath &lt;KitInstallersPath&gt; -ExpansionRoot &lt;Target Directory&gt; –LogFilePath &lt;LogFilePath&gt; -CatalogFile &lt;Filename.xml&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

    -   The *&lt;VSInstallerFilePath&gt;* is the path to the Visual Studio installation program (for example, Vs\_ultimate.exe) and directory that contains the product layout.
    -   The *&lt;KitInstallersPath&gt;* is the path to the WDK and SDK setup files.
    -   The *&lt;Target Directory&gt;* is the target directory for the extracted content.
    -   The *&lt;LogFilePath&gt;* is the target destination for the log file.
    -   *&lt;Filename.xml&gt;* is the name of the CatalogFile, which contains a list of Microsoft Windows installation files (MSI) to expand as part of the installation. The name of the file is files.xml.

    For example, the following command runs the script from BuildLabSupport directory and installs the build environment in C:\\BuildLabInstall directory.

    ``` syntax
    c:\BuildLabSupport>powershell -executionpolicy bypass -file Setup.ps1 -DeployBuildLab -VSInstallerPath c:\VSSetup -KitInstallersPath c:\Kits -E
    xpansionRoot C:\BuildLabInstall -CatalogFile  files.xml
    ```

<span id="build_step"></span><span id="BUILD_STEP"></span>4. Build Windows driver projects and solutions
--------------------------------------------------------------------------------------------------------

![](common/wedge.gif)**Using the build environment command script**

1.  Open a Command Prompt window. Locate the LaunchBuildEnv.cmd file located in the target directory (for example, C:\\BuildLabInstall).
2.  Launch the build environment by running **LaunchBuildEnv.cmd**.
3.  Use MSBuild commands to build your driver projects and solutions. For example:

    ``` syntax
    msbuild /t:clean /t:build .\MyDriver.vcxproj /p:Configuration="Win8.1 Debug" /p:Platform=Win32
    ```

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Building a Driver](building_a_driver.md)
* [MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262804)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Installing%20the%20WDK%20Build%20Environment%20in%20a%20Lab%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


