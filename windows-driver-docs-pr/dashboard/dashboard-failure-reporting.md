---
title: Hardware failure reporting using dashboard APIs
description: these asynchronous methods to access reporting data for your Win10/ Win 8.x driver errors and OEM hardware errors.
ms.topic: article
ms.localizationpriority: medium
ms.date: 04/05/2018
---

# Hardware failure reporting

Use these asynchronous methods to access reporting data for your Windows 8 and Windows 10 driver and OEM hardware errors. 

You can define reporting templates based on your needs, set a schedule and you will have data delivered to you at regular intervals. 

## Prerequisites 

To use this method, you need to first do the following: 
* If you have not done so already, complete all the [prerequisites](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services) for the Microsoft Store analytics API. 

* Obtain an [Azure AD access token](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services) to use in the request header for this method. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one. 

For more information, see Access analytics data using Microsoft Store services  

> [!IMPORTANT]
> As a reminder, the [Windows Analytics Agreement](https://go.microsoft.com/fwlink/?linkid=866941) states: “You must not store Personal Information for longer than thirty (30) days. Following such 30-day period, you will immediately destroy the Personal Information.” 

