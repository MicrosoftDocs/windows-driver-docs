---
title: MB Device Services
description: Windows 7 introduced a NDIS (Network Device Interface Specification) based driver model for supporting Mobile Broadband (MB) devices.
ms.assetid: 7F9DFD96-2221-4F64-AC51-F336CCBED6BF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Device Services


Windows 7 introduced a NDIS (Network Device Interface Specification) based driver model for supporting Mobile Broadband (MB) devices. Windows 8 expanded the model to implement a standardized hardware interface for USB-based Mobile Broadband devices. This hardware interface specification is referred as the Mobile Broadband Interface Model (MBIM).

Windows 8 provides an updated class driver that works with devices conforming to the MBIM specification. This model is referred to as the MB Class Driver. However, no class driver can support all of the functionality exposed by an MB device. In order to allow IHV partners to continue to innovate, the MB Class Driver provide mechanisms, such as the [**IMbnDeviceService interface**](https://msdn.microsoft.com/library/windows/desktop/hh780509) to allow IHVs to extend the behavior of the class driver functionality.

**Note**  Functionality to extend MB devices services is accomplished via a user-mode application, not a kernel-mode driver extension.

 

While the class driver introduced in Windows 7 featured limited MB device feature support, the MB Class Driver in Windows 8 added native support for some additional features such as USSD, EAP-SIM/AKA and USB selective suspend, and offers an extensible device representation and control mechanisms. The [Mobile broadband WinRT API overview](http://go.microsoft.com/fwlink/p/?linkid=242060) provides some additional information about extending device services.

The MB Class Driver in Windows 8 enables vertical solution providers to use the [Mobile Broadband API Interfaces](https://msdn.microsoft.com/library/windows/desktop/dd323268) to create enhanced user experiences that are outside of those provided by Windows. The extension mechanism is a way to augment, but not to replace, the functionality supported in the MB Class Driver itself. For example, an IHV can provide vendor-specific software that performs firmware updates on the device. Or, an IHV can provide vendor-specific software that provides value-add services such as SIM toolkit (STK) or Phonebook. The [AppContainer mobile broadband pin, connection and management](http://go.microsoft.com/fwlink/p/?linkid=320381) sample demonstrates Win32/COM Mobile Broadband APIs within the AppContainer to access and manage mobile broadband features.

In addition to providing a mechanism to extend the MB Class Driver' functionality, Windows also provides mechanisms to enable IHVs to deploy and install their value-add software through Windows Update (WU).

For more information see:

-   The "MBIM Service and CID Extensibility" section of the [Mobile Broadband Interface Model (MBIM) specification]( http://go.microsoft.com/fwlink/p/?linkid=320791)

 

 





