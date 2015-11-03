Preparing a Computer for Manual Driver Deployment
==============================================================================================================================

You can deploy a driver automatically or manually. In either case, you need to prepare the target computer first. Here we describe how to prepare the target computer if you choose to deploy your driver manually.

Typically the computer where you install and test a driver is separate from the computer where you develop and build the driver package. The computer where you build the driver is called the *host computer*, and the computer where you install and test the driver is called the *target computer* or the *test computer*. The process of moving the driver package to the target computer and installing the driver it is called *deploying the driver*.

1.  On the target computer, open a Command Prompt window as Administrator. Enter **bcdedit /set TESTSIGNING ON**. Reboot the target computer.
2.  Copy the [DevCon](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff544707) tool to a folder on the target computer (for example, c:\\Tools). The DevCon tool is included in the Windows Driver Kit (WDK). You can find it under the Tools directory (for example, C:\\Program Files (x86)\\Windows Kits\\8.1\\Tools\\x64\\devcon.exe).
3.  Create or get a certificate file that you can install on the target computer. For example, suppose you have used Microsoft Visual Studio to build the RAMDisk Storage Driver sample in the [code gallery](http://go.microsoft.com/fwlink/p/?LinkId=618052). The build process creates a certificate (.cer) file. The location of the certificate file varies depending on what you have specified for configuration and platform. For the RAMDisk sample, if your configuration is Win7 Debug and your platform is x64, then the certificate file, xx.cer, is in your solution folder under C++\\x64\\Win7Debug.
4.  Copy the certificate file to a folder on your target computer (for example c:\\Certificates).
5.  On the target computer, right click the certificate file, and choose **Install**. Work through the installation wizard.

When you build one of the WDK gallery samples, the build process creates a test-signing certificate. You need to install a test-signing certificate only once. If you have installed a certificate from a WDK gallery sample, you can install other gallery samples without installing a certificate again.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Preparing%20a%20Computer%20for%20Manual%20Driver%20Deployment%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


