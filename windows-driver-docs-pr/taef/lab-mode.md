---
title: Lab Mode
description: Lab Mode
ms.assetid: 127BDA2E-753E-4a71-89E2-6F31C4E5A263
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Lab Mode


By default, if a test crashes with an unhandled structured exception, the exception is reported and left for the OS-installed handler to process. This allows for JIT debugging during test development (a JIT debugger would pop-up, and allow you to investigate the crash).

For 'unattended' execution this behavior will block execution - typically leaving the JIT debugger or Windows Error Reporting UI showing. Te.exe supports the "/labMode" that doesn't hand structured exception handling off, but tears down the host process - allowing the Te.exe process to keep executing more tests, even though one or more tests in the run crash catastrophically.

Note that for '/inproc' execution the host process isn't torn down, since that would kill Te.exe and end the run. The behavior is to hand the structured exception to the OS installed handler - the same as the default behavior for out-of-process execution. This is consistent with the intent of "/inproc" - it should only be used for interactive debugging of a test.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Lab%20Mode%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




