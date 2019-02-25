---
title: Designing with Security Threat Models
description: Designing with Security Threat Models
ms.assetid: a505df1a-82c0-4e0b-88bb-d96654a098fb
keywords:
- security WDK file systems , threat models
- threat models WDK file systems
- security threat models WDK file systems
- threat models WDK file systems , about security threat models
- security threat models WDK file systems , about security threat models
- attacks WDK security
- I/O WDK security
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Designing with Security Threat Models


## <span id="ddk_designing_with_security_threat_models_if"></span><span id="DDK_DESIGNING_WITH_SECURITY_THREAT_MODELS_IF"></span>


In considering security, a common methodology is to create specific threat models that attempt to describe the types of attacks that are possible. This technique is useful when designing a file system or file system filter driver because it forces the developer to consider the potential attack vectors against a driver. Having identified potential threats, a driver developer can then consider means of defending against these threats in order to bolster the overall security of the driver component.

When considering security threat models, it is also important to differentiate between the actions drivers manage on behalf of user I/O requests (which are subject to security checks) and I/O operations initiated by drivers themselves (which are by default not subject to security checks). User-mode requests to one driver may also be passed on to another driver through internal FSCTL or IOCTL requests (the Srv.sys driver, for example), further complicating these issues.

For developers of kernel-mode drivers, the following important issues should be considered:

-   I/O operations initiated by drivers bypass security checks on the local system

-   I/O operations initiated by drivers bypass most parameter validation checks.

-   Drivers are part of the trusted computing base and thus can control the entire system.

Imagine, for example, a rogue program that was able to successfully load a driver on the system. This would provide it with tremendous control and would essentially compromise the system. If an application can exploit a feature of your driver to achieve the same thing, you have handed over control to the application and compromised the system.

Microsoft uses the "STRIDE" model when considering security:

-   S--[Spoofing Identity](spoofing-identity.md).

-   T--[Tampering with Data](tampering-with-data.md).

-   R--[Repudiation](repudiation.md).

-   I--[Information Disclosure](information-disclosure.md).

-   D--[Denial of Service](denial-of-service.md).

-   E--[Elevation of Privilege](elevation-of-privilege.md).

The basic principles here identify specific types of system compromise that can occur. Some of these principles have validity to drivers in general, but all have validity to file system and file system filter drivers.

 

 




