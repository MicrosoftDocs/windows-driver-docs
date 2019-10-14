---
title: Kernel Security Support Routines
description: Kernel Security Support Routines
ms.assetid: d8ee86dc-8327-4c0b-b916-cc6763d87178
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Kernel Security Support Routines

The following system-supplied kernel security support routines provided by the Kernel Security Driver (KSECDD.SYS) can be used by kernel-mode file system and file system (minifilter and legacy) filter drivers.

**Header File:** *ntifs.h*

**Prefix: Sec**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **SecLookupAccountName** | Accepts an account as input and retrieves a security identifier (SID) for the account and the name of the domain on which the account was found. |
| **SecLookupAccountSid** | Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found. |
| **SecLookupWellKnownSid** | Accepts a well-known security identifier (SID) type as input and retrieves the local security identifier (SID) for this well known SID. |
| **SecMakeSPN** | Creates a service provider name string that can be used when communicating with specific security service providers. |
| **SecMakeSPNEx** | Creates a service provider name string that can be used when communicating with specific security service providers. |
| **SecMakeSPNEx2** | Creates a service provider name string that can be used when it communicates with specific security service providers. |
