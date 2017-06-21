---
title: IOCTLs with FILE\_ANY\_ACCESS safe or sorry
description: FILE\_ANY\_ACCESS authorizes the I/O Manager to send an IRP for any caller that has a handle to the device, creating a possible path for malicious users to compromise the system. What's the alternative .
ms.assetid: FFCFA644-5ABB-4560-A10B-47BF1EAB84EA
ms.author: windowsdriverdev
ms.date: 06/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IOCTLs with FILE\_ANY\_ACCESS: safe or sorry?


**Last updated:**

-   May 27, 2007

FILE\_ANY\_ACCESS authorizes the I/O Manager to send an IRP for any caller that has a handle to the device, creating a possible path for malicious users to compromise the system. What's the alternative? The *RequiredAccess* bits in an IOCTL definition indicate the type of access that a caller must request when opening the file object that represents the device. The system-defined constant FILE\_ANY\_ACCESS, commonly used for driver IOCTLs and FSCTLs, authorizes the I/O Manager to send an IRP for any caller that has a handle to the device (that is, a handle to the file object that represents the target device object). FILE\_ANY\_ACCESS essentially allows unrestricted access to the target device.

Although FILE\_ANY\_ACCESS makes life easy for callers, it's risky for drivers because it can create a possible path for malicious users to compromise the system. For example, an IOCTL might put the device in a particular state that should only be in effect for legitimate reads and writes to the device. If the IOCTL's RequiredAccess is set to FILE\_ANY\_ACCESS, any caller could issue the IOCTL.

## <span id="_What_should_you_do__"></span><span id="_what_should_you_do__"></span><span id="_WHAT_SHOULD_YOU_DO__"></span> What should you do?


-   For new IOCTLs, don't specify FILE\_ANY\_ACCESS unless it's really necessary. Most requests need only FILE\_READ\_ACCESS or FILE\_WRITE\_ACCESS (or both—they can be OR'd together).

## <span id="related_topics"></span>Related topics


[Kernel-Mode Drivers: Fixing Common Driver Reliability Issues](http://download.microsoft.com/download/5/7/7/577a5684-8a83-43ae-9272-ff260a9c20e2/drvqa.doc)

[Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406)

Writing Secure Code, Chapter 23: General Good Practices
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20IOCTLs%20with%20FILE_ANY_ACCESS:%20safe%20or%20sorry?%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





