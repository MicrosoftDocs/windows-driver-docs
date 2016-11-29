---
title: Downloading a Checked Build of Windows
description: You have several options for downloading checked (debug) builds of Windows.
ms.assetid: e05c2232-af1a-4bf1-ac4b-273f33b007ba
keywords: ["checked builds WDK , installing"]
---

# Downloading a Checked Build of Windows


You have several options for downloading checked (debug) builds of Windows. You can download and install a partial checked build, using the checked operating system components provided with the Windows Driver Kit (WDK). If you are an MSDN subscriber, you can download the complete checked builds of Windows. You can also download checked builds of certain older versions of Windows (Windows XP and Windows Server 2003) from the Download Center.

-   [Downloading the checked build from the WDK](#downloading-the-checked-build-from-the-wdk-)
-   [MSDN Subscriber Downloads](#ddk-obtaining-the-checked-build-tools)
-   [Downloading checked builds from the Microsoft Download Center](#downloading-checked-builds--from-the-microsoft-download-center)

## <span id="Downloading_the_checked_build_from_the_WDK_"></span><span id="downloading_the_checked_build_from_the_wdk_"></span><span id="DOWNLOADING_THE_CHECKED_BUILD_FROM_THE_WDK_"></span>Downloading the checked build from the WDK


Starting with WDK for Windows Vista, the checked operating system image (kernel) and HAL, and associated PDB files are provided in the \\Debug\\*&lt;version&gt;*\\*&lt;platform&gt;* directory of the WDK.

For example, if you have WDK 8.1 installed, the path to the checked kernel and HAL for Windows 8.1 (x64) can be found in the C:\\Program Files (x86)\\Windows Kits\\8.1\\Debug\\winv6.3\\x64 directory.

For information about downloading the WDK, see [WDK and WinDbg downloads](http://go.microsoft.com/fwlink/p/?linkid=391348).

To use just the checked build components (kernel and HAL) in what is called a *partial checked build*, you need to first install the free build (retail version) of the operating system. You can also configure the computer to install the checked components at boot time, so that you can easily switch between checked and free builds on a single computer. For information about configuring your computer for a partial checked build, see [Installing Just the Checked Operating System and HAL (For Windows Vista and Later)](installing-just-the-checked-operating-system-and-hal--for-windows-vist.md).

The advantage of using a partial checked build instead of the complete checked build is that you get the benefit of the checked build for debugging how your driver interacts with the kernel, and the performance of the free (retail version) build for everything else. For more information about the Windows build options, see [Checked and Free Build Differences](checked-and-free-build-differences.md).

## <span id="ddk_obtaining_the_checked_build_tools"></span><span id="DDK_OBTAINING_THE_CHECKED_BUILD_TOOLS"></span>MSDN Subscriber Downloads


If you are an MSDN subscriber, you can download checked builds of the Windows operating system from the [MSDN Subscriber Downloads]( http://go.microsoft.com/fwlink/p/?linkid=391229) page. From the downloads page you can type in the search string for the Windows version you want (for example, "Windows 8.1 debug/checked") or you can select **Operating Systems** from the **Product Categories** selection box. To become an MSDN subscriber, go to the [MSDN Subscriptions](http://go.microsoft.com/fwlink/p/?linkid=391228) page.

## <span id="Downloading_checked_builds__from_the_Microsoft_Download_Center"></span><span id="downloading_checked_builds__from_the_microsoft_download_center"></span><span id="DOWNLOADING_CHECKED_BUILDS__FROM_THE_MICROSOFT_DOWNLOAD_CENTER"></span>Downloading checked builds from the Microsoft Download Center


You can also download some checked builds for older versions of Windows from the [Microsoft Download Center]( http://go.microsoft.com/fwlink/p/?linkid=391352). In the search box for the Download Center, search for **checked build**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Downloading%20a%20Checked%20Build%20of%20Windows%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




