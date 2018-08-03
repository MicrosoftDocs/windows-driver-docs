---
title: Active Directory
author: windows-driver-content
description: Active Directory
ms.assetid: 8524c708-7d21-4657-8af5-975894808d8e
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Active Directory


The DSM device must interact with Active Directory as follows:

-   By retrieving domain-specific credentials from a user (for example, from a card reader attached to the DSM device) and sending them to Active Directory.

-   By querying for and retrieving a user object (specifically the user SID) from Active Directory.

-   By querying for and retrieving the list of Scan Processes available to the user from the Active Directory.

-   By retrieving the details of a selected Scan Process from the Active Directory.

 

 




