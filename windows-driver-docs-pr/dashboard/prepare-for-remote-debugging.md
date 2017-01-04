---
title: Prepare for Remote Debugging
description: Prepare for Remote Debugging
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 744c9ff6-77a8-4bb0-ada8-502f22aa6558
---

# Prepare for Remote Debugging


With the Windows Remote Debugging (Windows RD) client, developers from Microsoft and your company can collaborate to debug kernel mode failures.

Before using the Windows Remote Debugging client, you must:

1.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account.

    **Note**  
    If you don't have a dashboard account, see [Before You Sign In](https://msdn.microsoft.com/library/windows/hardware/br230782.aspx) for instructions to create one.

     

2.  Have permission to host a session or join a session as a participant. For more information, see the Permissions section in this topic.

3.  Install the Windows RD client on a computer with the following system requirements:

    -   An Internet connection.

    -   A TCP connection to the host computer when you are running a remote session within your corporate network.

    -   Any of the following operating systems (either 32-bit or 64-bit):

        -   Windows 10
        -   Windows 8.1

        -   Windows 8

        -   Windows 7

        -   Windows Server 2016
        -   Windows Server 2012

        -   Windows Vista

        -   Windows Server 2008

    -   At least 1 megabyte (MB) of available disk space.

    -   Windows Live Essentials.

        If Windows Live Essentials isn't installed, the current version is added automatically during the installation of the Windows RD client.

    -   Microsoft .NET Framework 3.0.

        If Microsoft® .NET Framework isn't installed, you will be given an opportunity to download it during the installation of the Windows RD client.

4.  Install the Debugging Tools for Windows package if you are going to host a session.

    The Kernel Debugger (KD) is the only debugger that is currently supported by the Windows RD client.

## <span id="Permissions"></span><span id="permissions"></span><span id="PERMISSIONS"></span>Permissions


Before you can use the Windows RD client, you must have permission either to host or join a session.

**To obtain permission**

1.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account. This account must be an Administrator for your organization in the Dashboard.

2.  On the left side of the window, click **Administration**.

3.  On the **Administration** page, under **Your profile**, click **Request permissions from your admin**.

4.  On the **Permissions** tab, under **Windows Remote Debugging**, select either **Host Sessions**, **Join Sessions**, or both. Click **Update**.

After your administrator has approved your request, you can start using the Windows Remote Debugging client.

## <span id="BKMK_install"></span><span id="bkmk_install"></span><span id="BKMK_INSTALL"></span>Installation


After you have confirmed that you have permission to host or attend a remote debugging session, you can install Windows Remote Debugging.

If you are going to host a session, you must use KD as the debugger. KD is available when you install the Debugging Tools for Windows (DTW). The Debugging Tools for Windows package is available as an optional component of the Windows Software Development Kit (SDK). You don't need to install the complete Windows SDK.

**To install Windows Remote Debugging**

1.  Sign in to the Dashboard from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account.

2.  On the left navigation bar, click **Remote Debugging**.

3.  On the **Remote Debugging** page, in the **Download** box, click the **Windows Remote Debugging Client** link to download the latest version.

**To install the Debugging Tools for Windows**

-   [Download the Debugging Tools for Windows package](http://go.microsoft.com/fwlink/p/?LinkId=248842).

Full instructions about how to install the tools and configure the software and hardware, on both host and target computers, can be found in the .chm file that is part of the DTW package.

## <span id="related_topics"></span>Related topics


[Host a Remote Debugging Session](https://msdn.microsoft.com/library/windows/hardware/br230799.aspx)

[Join a Remote Debugging Session](https://msdn.microsoft.com/library/windows/hardware/br230787.aspx)

[Known Issues with the Remote Debugging Client](https://msdn.microsoft.com/library/windows/hardware/br230769.aspx)

[Take Part in a Remote Debugging Session](https://msdn.microsoft.com/library/windows/hardware/br230804.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Prepare%20for%20Remote%20Debugging%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





