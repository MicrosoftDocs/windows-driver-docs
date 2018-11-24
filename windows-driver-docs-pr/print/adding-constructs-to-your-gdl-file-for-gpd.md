---
title: Adding Constructs to Your GDL File for GPD
description: Adding Constructs to Your GDL File for GPD
ms.assetid: a0ce5a46-152f-47f3-9246-c272224d4be9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Constructs to Your GDL File for GPD


To support autoconfiguration, you must add constructs to a GDL file by using the following new keywords: \***BidiQuery**, \***QueryString**, \***BidiResponse**, \***ResponseType**, \***ResponseData**, and \***BidiValue**. You can use these keywords to specify a bidi schema request that is associated with one option of a feature and the possible responses to that option.

A \***Feature** construct can contain a single \***BidiQuery** construct, which serves as a container for a \***QueryString** instance. The query string in a \***Feature** construct instance is a Unicode string that consists of the bidi communications schema path to the feature that is being queried appended with the name of the particular property of the feature.

A \***Feature** construct can also contain a single \***BidiResponse** construct, which serves as a container for one \***ResponseType** instance and an optional \***ResponseData** instance.

Each \***Option** construct that is associated with the \***Feature** construct must contain a \***BidiValue** instance that includes a string representation of the response that is appropriate to that \***Option**.

The following examples show how to add the appropriate constructs to your GDL file, based on the features listed in your GPD file. The first two examples consists of a GPD sample and a GDL sample with the constructs necessary to support autodetection or autoconfiguration of a particular installable feature. The third example provides a GDL sample for autodetection of the hard drive, and assumes the existence of a GPD feature definition for the hard drive.

[Autodetecting the Duplex Unit for GPD](autodetecting-the-duplex-unit-for-gpd.md)

[Autoconfiguring the Printer's Memory for GPD](autoconfiguring-the-printer-s-memory-for-gpd.md)

[Autodetecting the Printer's Hard Drive for GPD](autodetecting-the-printer-s-hard-drive-for-gpd.md)

 

 




