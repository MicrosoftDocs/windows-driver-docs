---
title: Windows 5G MBIM Interface
description: Windows 5G MBIM Interface
keywords:
- Windows 5G MBIM Interface
ms.date: 03/01/2021
ms.localizationpriority: medium
ms.custom: 19H1
---

# Windows 5G MBIM Interface

As of Windows 10, version 1903, 5G on the whole is still developing. From a network deployment perspective, 5G is expected to be deployed in two major phases: 

* In Phase 1, most mobile network operators are expected to deploy 5G with the addition of 5G radio to the existing LTE radio and EPC core deployments, commonly known “nonstandalone 5G” networks.  

* In Phase 2, mobile network operators are expected to replace EPCs and NGCs and densify the 5G radio deployment in parallel to enable true “standalone”, or NR-NGC-based 5G networks. Phase 2 interface extensions are not in scope in this topic or Windows release. 

Interface extensions to support basic Phase 1 network requirements, or ”nonstandalone” EPC-based 5G networks, was introduced in Windows 10, version 1903. In order to be extensible and fully backward compatible with legacy modems, a new Microsoft MBIM extension version (2.0) is introduced. 

The new Microsoft MBIM extension version is required because the [MBIM 1.0 errata specification](https://www.usb.org/sites/default/files/MBIM10Errata1_073013.zip) has a mechanism to add and advertise optional CIDs, but it lacks a mechanism to change the existing CIDs (new payloads or modified payload) or to introduce changes in any aspect that cannot be accommodated by optional CIDs. Each payload may consist of fixed sized members or dynamic sized (offset/size pairs) members. If one or more  dynamically sized members exist, then the last member has a variable size buffer.  

This spec also adds a new CID for the host to advertise its MBIM Release version and Extensions Release version to MBIM devices. For legacy drivers that are already in the field, this CID is optional so backward compatibility is fully maintained.  For more details, see [MBIMEx 2.0 – 5G NSA support](mbimex-2.0-5g-nsa-support.md). 