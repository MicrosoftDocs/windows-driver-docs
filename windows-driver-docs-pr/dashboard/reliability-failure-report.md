---
title: Reliability Measure Failure Report
description: Describes the Reliability Measure Failure report provided upon cancellation
ms.topic: article
ms.date: 07/12/2021
ms.localizationpriority: medium
---

# Plug and Play extended flight report

If your driver is cancelled due to a Reliability Measure failure, you will start to receive a new report detailing the specifics of the failure.

## Location of the report

When a driver completes flighting, a bug is created and assigned to you. The bug includes a *Decision Snapshot*, a report on the state of the measures at the time of flight completion. If the driver is cancelled due to a Reliability measure failing during release monitoring, the same bug includes an *Reliability Measure Failure Report*. It is added to the RejectionReports.zip file as an attachment to that bug. Inside the zip file, the report filename is * ReliabilityMeasureReport.pdf.*

![Screenshot of bug attachment with the RejectionReports.zip file attached that contains the PnP_Extended_Flight_Report.pdf](images/RejectionReports.png)

## How to read the report

The report contains the following sections:

1. [Title](#title)
1. [Summary](#summary-and-instructions)
1. [Driver Level Details](#driver-level-details)
1. [Cohort Level Details](#cohort-level-details)
1. [Failure Hash Reported From Drivers](#failure-hash-reported-from-drivers)
1. [Latest Cabs](#latest-cabs)

### Title

The Title section describes the driver, including the submitter company name, the date the report was generated, the shipping label number, the driver name, and the driver version.

![Screenshot of the Title section that includes the submitter company name, report date, shipping label, driver name, and driver version.](images/PnP_report_title.png)

### Summary

The Summary section provides basic information about what type of analysis was done and what you can do to address the issue. 

![Screenshot of the Summary and Instructions section.](images/reliability-report-summary.png)

### Driver Level Details Data

The Driver Level Details Section provides details specific to the Reliability Measure(s) failures that led the driver to be rejected. 

In this section, you will find:

- The Measure ID (to look it up in the Measure Dictionary and the Flight Report) 
- The Measure name 
- The result of the measure at the time of the report 
- The passing criteria 
- The status of the measure 
- The number of machines that have adopted the driver and were used to calculate the measure 
- Timeline with the evolution of measure result (purple) and passing criteria (red) over time 

2 potentially evaluated metrics:  

- **Measure 26118008**: Percent of machines reported BSOD crashes in last 7 days 
- **Measure 26118015**: Percent of machines that reported a live kernel dump in last 7 days 

![Screenshot of the Driver Level Details section.](images/reliability-report-driver-level-md.png)

### Cohort Level Details

This section includes details about the reliability failures that were found, at a cohort level. The section will repeat for each failing cohort that is found. 

The section first lists a targeting cohort (Hardware ID, CHID, and OS version) where the failure was found. This is followed by the list of measures that failed for that targeting cohort, including: 

- The Measure ID (to look it up in the Measure Dictionary and the Flight Report). 
- The Measure name 
- The result of the measure at the time of the report 
- The passing criteria 
- The status of the measure 
- The number of machines in that cohort that have adopted the driver and were used to calculate the measure. 
- Timeline with the evolution of measure result (purple) and passing criteria (red) over time 


2 potentially evaluated metrics:  

- **Measure 26118008**: Percent of machines reported BSOD crashes in last 7 days 
- **Measure 26118015**: Percent of machines that reported a live kernel dump in last 7 days 

 

***Note: All small cohorts (< 500 instance count) are merged into “other” cohort***

![Screenshot of the Cohort Level Details section.](images/reliability-report-cohort.png)

### Failure Hash Reported From Drivers

This section provides additional information on Crash Types and Failure Hash reported from the current driver 

![Screenshot of the Supplemental Data section.](images/reliability-report-failure-hash.png)

### Latest Cabs

This sections provides additional information on the latest cabs from different OS

![Screenshot of the Additional References section.](images/reliability-report-latest-cabs.png)
