---
title: EmailConfig.SendToAddresses
description: EmailConfig.SendToAddresses
ms.assetid: 1124d5b9-086f-452c-93e6-a8ceb51bf43a
keywords: ["EmailConfig.SendToAddresses"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EmailConfig.SendToAddresses


The **SendToAddresses** element defines the set of destination email addresses that the email processing filter will use to send the scanned images for the current PostScan job.

The **SendToAddresses** element can contain one or more **EmailAddress** elements. The DSM Scan Server will try to send the email message, with the attached scanned images, to each of the email addresses specified in an **EmailAddress** element.

The **SendToAddresses** element supports the following attribute:

[EmailConfig.SendToAddresses.CanAddAddresses](emailconfig-sendtoaddresses-canaddaddresses.md)

The **SendToAddresses** element supports the following sub-element

[EmailConfig.SendToAddresses.EmailAddress](emailconfig-sendtoaddresses-emailaddress.md)

 

 





