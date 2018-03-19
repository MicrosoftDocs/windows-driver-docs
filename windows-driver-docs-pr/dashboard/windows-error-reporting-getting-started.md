---
title: Windows Error Reporting Getting Started
description: Windows Error Reporting Getting Started
ms.assetid: 74b2522a-c6e5-4079-83b8-57ccc14b58f7
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows Error Reporting: Getting Started


Windows Error Reporting (WER) is a set of Windows technologies that capture software crash and failure data from end users. This data is analyzed to create a list of top user-mode (software) and kernel-mode (operating system) failures associated with a company’s mapped products. Through the Hardware Dev Center hardware dashboard website, software and hardware vendors can access these reports and use them to analyze, fix and respond to these failures. This service is available for all products, even those that do not qualify for the Microsoft Certified Products list—although we strongly recommend that you submit your products to the [Windows Hardware Compatibility Program](https://msdn.microsoft.com/library/windows/hardware/dn922588).

**Tip**  
Over time, Microsoft has found that across all the issues that exist on the affected Windows platforms and the number of incidents received:

-   Fixing 20 percent of the top-reported bugs can solve 80 percent of customer issues.

-   Addressing 1 percent of the bugs would address 50 percent of the customer issues.

 

**Note**  
To access WER reporting service, as well as Hardware Dev Center hardware dashboard, you need a standard code signing certificate. To learn more about code signing certificates, see [Get a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/hh801887.aspx).

 

## <span id="Viewing_reports"></span><span id="viewing_reports"></span><span id="VIEWING_REPORTS"></span>Viewing reports


Once you have a Hardware Dev Center hardware dashboard account, you can log in to view the top user-mode and kernel-mode failures associated with your company’s mapped products. For more information about the options available in these reports, see [Browse Reports](https://msdn.microsoft.com/library/windows/hardware/br230773.aspx).

## <span id="Creating_responses"></span><span id="creating_responses"></span><span id="CREATING_RESPONSES"></span>Creating responses


After you’ve analyzed a specific user-mode or kernel-mode failure, and created a fix or other solution, you can then create a response to be delivered through Windows Action Center to your customers. After this response is in place, customers who experience this problem (including those who experienced the problem in the past) will receive your solution.

By taking advantage of the WER feedback loop, you can provide information to your customers to help solve their problems and to reduce your company's support costs. For more information about how to create responses, see [Create Responses](https://msdn.microsoft.com/library/windows/hardware/br230774.aspx).

## <span id="WER_resources"></span><span id="wer_resources"></span><span id="WER_RESOURCES"></span>WER resources


-   [Debugging in the (Very) Large: Ten Years of Implementation and Experience (PDF – 938 KB)](http://www.sigops.org/sosp/sosp09/papers/glerum-sosp09.pdf)

-   [How WER collects and classifies error reports](https://msdn.microsoft.com/library/windows/hardware/dn641147.aspx)

-   [Debugging OCA minidump files](https://msdn.microsoft.com/library/windows/hardware/dn641143.aspx)

-   [WER Services blog](http://blogs.msdn.com/b/wer/)

-   [Privacy Statement for the Microsoft Error Reporting Service](http://watson.microsoft.com/dw/1033/dcp.asp)

-   [Questions about SysDev online submission website](mailto:winqual@microsoft.com)

## <span id="Error_classification_resources"></span><span id="error_classification_resources"></span><span id="ERROR_CLASSIFICATION_RESOURCES"></span>Error classification resources


-   [KeRegisterBugCheckCallback routine](http://msdn.microsoft.com/library/ff553105.aspx)

-   [Windows Vista Privacy Notice Highlights](http://go.microsoft.com/fwlink/p/?LinkId=618595)

 

 





