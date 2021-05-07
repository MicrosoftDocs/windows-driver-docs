---
title: WDI_TLV_OWE_DH_IE
description: WDI_TLV_OWE_DH_IE is a TLV that must be included in the association request sent by the station when the auth type is OWE. 
ms.date: 05/07/2021
keywords:
 - WDI_TLV_OWE_DH_IENetwork Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_OWE\_DH\_IE

WDI\_TLV\_OWE\_DH\_IE is a Diffie-Hellman Extension IE blob that must be included in the association request sent by the station when auth type is OWE. This is applicable to any BSSID that the device would associate with and should be included in addition to the other associated req vendor IEs.

## TLV Type

0x16A

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | An array of UINT8 elements that contains the IEs that must be included in association requests sent by the port. These are applicable to any BSSID that the device associates with. They should be used in addition to the common and BSSID specific IEs. |

## Requirements

| &nbsp; | &nbsp; |
| ------ | ------ |
| **Minimum supported client** | Windows 10, version 2004 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.hpp |
