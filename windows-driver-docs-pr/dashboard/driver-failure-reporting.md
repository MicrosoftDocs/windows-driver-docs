---
title: Driver failure reporting
description: The Driver failure report in the Windows Hardware Dev Center dashboard lets you get performance data related to your driver, including crashes and other events.
ms.assetid: F98F61EF-6C4A-400A-BA01-B79C72A7993A
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver failure reporting


The Driver failure report in the Windows Hardware Dev Center dashboard lets you get data related to the performance and quality of your driver, including crashes and unresponsive events. Where applicable, you can view stack traces for further debugging.

## <span id="Apply_filters"></span><span id="apply_filters"></span><span id="APPLY_FILTERS"></span>Apply filters


Gives you the ability to organize and filter all data within the report by the following:

-   Submission
-   OS version
-   Market
-   Architecture
-   Flight ring
-   OEM Name
-   OEM Model
-   Device type
-   Driver name

The information in the charts listed below will reflect the period of time selected in the **Apply filters** section. By default this includes data for all of your package versions, unless you've used **Apply filters** to choose only one.

## <span id="Failure_hits"></span><span id="failure_hits"></span><span id="FAILURE_HITS"></span>Failure hits


The **Failure hits** chart shows the number of daily crashes and events that customers experienced in the last 30 days. Each type of event that your app experienced is tracked separately, categorized by **live kernel event** and **system crash**.

## <span id="Failure_breakdown"></span><span id="failure_breakdown"></span><span id="FAILURE_BREAKDOWN"></span>Failure breakdown


You can pivot the failure count by different attributes:

-   driver version
-   OS version
-   flight ring
-   OEM Model
-   Device type
-   Architecture

## <span id="Failures"></span><span id="failures"></span><span id="FAILURES"></span>Failures


The **Failures** chart shows the total number of failures for the selected filters. By default, the report displays failures in descending order of **hits**. You can reverse this order by toggling the arrow in the **Hits** column of this chart. Additionally, each failure is shown with its percentage of the total number of failures. To display the Failure details report for a particular failure, select the failure name. The Failure details report includes the number of failure hits over the last month, and a failure log listing a link to the cab download, and several occurrence details:

-   date
-   package version
-   device type
-   device model
-   OS build

 

 

