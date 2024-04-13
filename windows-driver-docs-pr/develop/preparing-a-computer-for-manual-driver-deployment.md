---
title: Preparing a Computer for Manual Driver Deployment
description: Describes how to prepare the target computer before deploying a driver manually.
ms.date: 06/04/2018
---

# Preparing a Computer for Manual Driver Deployment

You can deploy a driver automatically or manually. In either case, you need to prepare the target computer first. Here we describe how to prepare the target computer if you choose to deploy your driver manually.

Typically the computer where you install and test a driver is separate from the computer where you develop and build the driver package. The computer where you build the driver is called the *host computer*, and the computer where you install and test the driver is called the *target computer* or the *test computer*. The process of moving the driver package to the target computer and installing the driver it is called *deploying the driver*.

1.  On the target computer, open a Command Prompt window as Administrator. Enter **bcdedit /set TESTSIGNING ON**. Reboot the target computer.
2.  Copy the [DevCon](../devtest/devcon.md) tool to a folder on the target computer (for example, c:\\Tools). The DevCon tool is included in the Windows Driver Kit (WDK). You can find it under the Tools directory (for example, C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\x64\\devcon.exe).
3.  Create or get a certificate (.cer) file that you can install on the target computer. For example, when you build one of the WDK sample drivers, the build process creates a certificate (.cer) file. The location of the certificate file varies depending on what you have specified for configuration and platform. For example, if your configuration is Win7 Debug and your platform is x64, then the certificate file is in your solution folder under C++\\x64\\Win7Debug.
4.  Copy the certificate file to a folder on your target computer (for example c:\\Certificates).
5.  On the target computer, right-click the certificate file, and choose **Install**. Work through the installation wizard. The [test certificates](../install/makecert-test-certificate.md) used to embed signatures in driver files and to sign a [driver package](../install/driver-packages.md) [catalog file](../install/catalog-files.md) must be added to the [Trusted Root Certification Authorities certificate store](../install/trusted-root-certification-authorities-certificate-store.md) and the [Trusted Publishers certificate store](../install/trusted-publishers-certificate-store.md). For more information about installing the certificate on the target computer, see [Installing a Test Certificate on a Test Computer](../install/installing-a-test-certificate-on-a-test-computer.md).

When you build one of the WDK driver samples, the build process creates a test-signing certificate. You need to install a test-signing certificate only once. If you have installed a certificate from a WDK driver sample, you can install other driver samples without installing a certificate again.
