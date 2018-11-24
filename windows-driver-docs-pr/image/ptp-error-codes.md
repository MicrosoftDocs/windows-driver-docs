---
title: PTP Error Codes
description: PTP Error Codes
ms.assetid: 4d7ad081-fc0b-4a9e-8f17-a0c98fa4fa50
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PTP Error Codes





When the Microsoft PTP WIA minidriver detects an error, it passes the response code to WIA. If the PTP camera returns a response other than 0x2001 (OK), the WIA minidriver returns the response code wrapped as an HRESULT error code. The format of the error code is 0x8004XXXX, where XXXX represents the four hexadecimal digits of the response code. This is very useful for WIA applications that are designed to work with specific PTP cameras. The error/status information is preserved for rich status to be reported to the end user.

 

 




