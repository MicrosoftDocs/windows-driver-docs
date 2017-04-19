---
ms.assetid: 9B4E7164-A63A-4E47-AFD1-BEBDC3761054
title: Preparing a Computer for Manual Driver Deployment
description: Describes how to prepare the target computer before deploying a driver manually.
---

# Preparing a Computer for Manual Driver Deployment

You can deploy a driver automatically or manually. In either case, you need to prepare the target computer first. Here we describe how to prepare the target computer if you choose to deploy your driver manually.

Typically the computer where you install and test a driver is separate from the computer where you develop and build the driver package. The computer where you build the driver is called the *host computer*, and the computer where you install and test the driver is called the *target computer* or the *test computer*. The process of moving the driver package to the target computer and installing the driver it is called *deploying the driver*.

1.  On the target computer, open a Command Prompt window as Administrator. Enter **bcdedit /set TESTSIGNING ON**. Reboot the target computer.
2.  Copy the [DevCon](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff544707) tool to a folder on the target computer (for example, c:\\Tools). The DevCon tool is included in the Windows Driver Kit (WDK). You can find it under the Tools directory (for example, C:\\Program Files (x86)\\Windows Kits\\8.1\\Tools\\x64\\devcon.exe).
3.  Create or get a certificate file that you can install on the target computer. For example, suppose you have used Microsoft Visual Studio to build the RAMDisk Storage Driver sample in the [code gallery](http://go.microsoft.com/fwlink/p/?LinkId=618052). The build process creates a certificate (.cer) file. The location of the certificate file varies depending on what you have specified for configuration and platform. For the RAMDisk sample, if your configuration is Win7 Debug and your platform is x64, then the certificate file, xx.cer, is in your solution folder under C++\\x64\\Win7Debug.
4.  Copy the certificate file to a folder on your target computer (for example c:\\Certificates).
5.  On the target computer, right click the certificate file, and choose **Install**. Work through the installation wizard.

When you build one of the WDK gallery samples, the build process creates a test-signing certificate. You need to install a test-signing certificate only once. If you have installed a certificate from a WDK gallery sample, you can install other gallery samples without installing a certificate again.

 

 





