---
title: Adding Constructs to Your GDL File for PPD
description: Adding Constructs to Your GDL File for PPD
ms.assetid: 981952b2-cc13-4c62-935b-74e749278c0f
keywords:
- constructs WDK printer autoconfig
- PPD files WDK autoconfiguration , constructs
- in-box autoconfiguration support WDK printer , constructs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Constructs to Your GDL File for PPD


To support autoconfiguration, you must add constructs to a GDL file by using the following new keywords: \***BidiQuery**, \***QueryString**, \***BidiResponse**, \***ResponseType**, \***ResponseData**, and \***BidiValue**. You can use these keywords to specify a bidi schema request that is associated with one option of a feature and the possible responses to that option.

A \***Feature** construct can contain a single \***BidiQuery** construct, which serves as a container for a \***QueryString** instance. The query string in a \***Feature** construct instance is a Unicode string that consists of the bidi communications schema path to the feature that is being queried appended with the name of the particular property of the feature.

A \***Feature** construct can also contain a single \***BidiResponse** construct, which serves as a container for one \***ResponseType** instance and an optional \***ResponseData** instance.

Each \***Option** construct that is associated with the \***Feature** construct must contain a \***BidiValue** instance that includes a string representation of the response that is appropriate to that \***Option**.

The following examples show how to add the appropriate constructs to your GDL file, based on the features listed in your PPD file. The first two examples consists of a PPD sample and a GDL sample with the constructs necessary to support autodetection or autoconfiguration of a particular installable feature. The third example provides a GDL sample for autodetection of the hard drive, and assumes the existence of a PPD feature definition for the hard drive.

[Autodetect the Duplex Unit for PPD](autodetect-the-duplex-unit-for-ppd.md)

[Autoconfigure the Printer's Memory for PPD](autoconfigure-the-printer-s-memory-for-ppd.md)

[Autodetect the Printer's Hard Drive for PPD](autodetect-the-printer-s-hard-drive-for-ppd.md)

 

 




