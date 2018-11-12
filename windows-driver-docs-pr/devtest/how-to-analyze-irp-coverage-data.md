---
title: How to Analyze IRP Coverage Data
description: How to Analyze IRP Coverage Data
ms.assetid: 71b87948-8e69-4b4a-9546-ea27e96a4bf8
keywords:
- Driver Coverage Toolkit WDK , analyzing data
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Analyze IRP Coverage Data


**Note**  The Driver Coverage Toolkit is no longer needed in Windows 10 and the installer is no longer included in the WDK. To perform tasks described here in Windows 10, instead use [Driver Verifier](driver-verifier.md) and [IRP Logging](irp-logging.md).

 

This topic provides guidelines to help you analyze IRP coverage data. For guidelines to help you collect IRP coverage data, see [How to Collect IRP Coverage Data](how-to-collect-irp-coverage-data.md).

After you have collected the IRP coverage data for one or more devices on a test computer, you can use the [Coverage Tests (Device Fundamentals)](coverage-tests--device-fundamentals-.md) to produce reports from this data. These reports show the count of individual I/O request packets (IRPs) that entered or left the driver stack for a specified device. The types of IRPs that did not enter or leave the driver stack are also reported.

For this topic, we use, as an example, a report produced from IRP coverage data that was enabled for a device node (devnode) on a test computer. The devnode is 9740, and IRP coverage was previously enabled for the devnode by running the **Enable IRP coverage data collection** tool on the test computer.

For information about setting up the WDK and the Visual Studio test environment, see [How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime). For information about selecting and configuring tests and tool parameters, see [How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests) and [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests).

After the IRP coverage data has been collected, an IRP coverage report for this devnode is produced by running the **Display collected IRP coverage data** tool on the test computer.

```
Drvcov /C 9740
```

The IRP coverage report has four sections:

<span id="Report_Header_______"></span><span id="report_header_______"></span><span id="REPORT_HEADER_______"></span>**Report Header**   
This section provides information about the device, whose IRP coverage data is shown in the report.

The IRP coverage report for devnode 9740 is shown below.

```
Getting coverage data
Data source
 Source Type:  Driver
 Source Name:  \\.\DrvcovControl1
 Device
   Friendly Name : Disk drive 
   Class Name    : DiskDrive 
   Device ID     : IDE\DISKST9320421AS_____________________________SD13____\5&37E07111&0&0.0.0 
   Device #      : 1 
 Devnode #     : 9740
```

<span id="IRP_Major__MJ__and_Minor__MN__Coverage_Data_______"></span><span id="irp_major__mj__and_minor__mn__coverage_data_______"></span><span id="IRP_MAJOR__MJ__AND_MINOR__MN__COVERAGE_DATA_______"></span>**IRP Major (MJ) and Minor (MN) Coverage Data**   
This section shows the counters for the IRP MJ and their subordinate MN function codes that are processed by the driver for the specified devnode during the IRP coverage period. The Driver Coverage toolkit monitors and reports on 52 IRP MJ and MJ function codes.

This section provides information about the following:

-   The counters for each IRP MJ and MN function codes processed by the driver. These counters can be used to determine which IRPs had adequate test coverage and which may need more coverage.

-   A list of the IRP MJ and MN function codes that were not processed by the driver. This information is very important and can provide insight about deficiencies in your code coverage tests.

**Note**  Decisions about which IRPs to test is dependent on your driver and the IRPs the driver supports. The IRP MJ and MN coverage data can help you evaluate the efficiency of your code coverage tests for your driver.

 

The IRP MJ and MN coverage data for devnode 9740 is shown in the following example:

```
|--------------------------------------------------------|
| MJ & MN Device irp coverage                            |
|--------------------------------------------------------|
| IRPS covered     19                      |  # of times |
|--------------------------------------------------------|
| Unknown                                  |           5 | 
| PNP\QUERY_RESOURCE_REQUIREMENTS          |           3 | 
| PNP\FILTER_RESOURCE_REQUIREMENTS         |           3 | 
| PNP\START_DEVICE                         |           8 | 
| DEVICE_CONTROL                           |         293 | 
| READ                                     |        2543 | 
| PNP\QUERY_CAPABILITIES                   |           3 | 
| PNP\QUERY_PNP_DEVICE_STATE               |           7 | 
| CREATE                                   |          44 | 
| CLEANUP                                  |          45 | 
| CLOSE                                    |          43 | 
| WRITE                                    |        2488 | 
| WMI\REGINFO_EX                           |           5 | 
| WMI\REGINFO                              |           5 | 
| FLUSH_BUFFERS                            |        1491 | 
| PNP\QUERY_DEVICE_RELATIONS\Target        |          23 | 
| WMI\QUERY_ALL_DATA                       |           6 | 
| POWER\QUERY_POWER\SYSTEM                 |           2 | 
| SHUTDOWN                                 |           2 | 
|--------------------------------------------------------|
| IRPS NOT covered     33                  |             |
|--------------------------------------------------------|
| INTERNAL_DEVICE_CONTROL                  |             | 
| POWER\WAIT_WAKE                          |             | 
| POWER\SET_POWER\SYSTEM                   |             | 
| POWER\SET_POWER\DEVICE                   |             | 
| POWER\QUERY_POWER\DEVICE                 |             | 
| WMI\QUERY_SINGLE_INSTANCE                |             | 
| WMI\CHANGE_SINGLE_INSTANCE               |             | 
| WMI\CHANGE_SINGLE_ITEM                   |             | 
| WMI\ENABLE_EVENTS                        |             | 
| WMI\DISABLE_EVENTS                       |             | 
| WMI\ENABLE_COLLECTION                    |             | 
| WMI\DISABLE_COLLECTION                   |             | 
| WMI\EXECUTE_METHOD                       |             | 
| PNP\QUERY_REMOVE_DEVICE                  |             | 
| PNP\REMOVE_DEVICE                        |             | 
| PNP\CANCEL_REMOVE_DEVICE                 |             | 
| PNP\STOP_DEVICE                          |             | 
| PNP\QUERY_STOP_DEVICE                    |             | 
| PNP\CANCEL_STOP_DEVICE                   |             | 
| PNP\QUERY_DEVICE_RELATIONS\Bus           |             | 
| PNP\QUERY_DEVICE_RELATIONS\Eject         |             | 
| PNP\QUERY_DEVICE_RELATIONS\Removal       |             | 
| PNP\QUERY_INTERFACE                      |             | 
| PNP\QUERY_RESOURCES                      |             | 
| PNP\QUERY_DEVICE_TEXT                    |             | 
| PNP\READ_CONFIG                          |             | 
| PNP\WRITE_CONFIG                         |             | 
| PNP\EJECT                                |             | 
| PNP\SET_LOCK                             |             | 
| PNP\QUERY_ID                             |             | 
| PNP\QUERY_BUS_INFORMATION                |             | 
| PNP\DEVICE_USAGE_NOTIFICATION            |             | 
| PNP\SURPRISE_REMOVAL                     |             | 
|--------------------------------------------------------|
| Stats                                                  |
|--------------------------------------------------------|
| Total IRP count        :     52                        |
| Covered IRP count      :     19                        |
| NOT Covered IRP count  :     33                        |
| Covered IRP %          :     36.54%                    |
| NOT Covered IRP %      :     63.46%                    |
|--------------------------------------------------------|
```

<span id="IRP_MJ_Coverage_Data_______"></span><span id="irp_mj_coverage_data_______"></span><span id="IRP_MJ_COVERAGE_DATA_______"></span>**IRP MJ Coverage Data**   
This section shows the counters for only the IRP MJ function codes that are processed by the driver for the specified devnode during the IRP coverage period. The Driver Coverage toolkit monitors and reports on 13 IRP MJ function codes.

This section provides information about the following:

-   The counters for each IRP MJ function code that was processed by the driver. You can use these counters to determine which IRPs had adequate test coverage and which may need more coverage.

-   A list of the IRP MJ function codes that were not processed by the driver. This information is very important and can provide insight about deficiencies in your code coverage tests.

As with the IRP MJ and MN coverage data, the data in this section can be used to analyze the efficiency of your code coverage tests. In particular, this data shows how well the driver's dispatch routines for each IRP MJ function code were tested.

The IRP MJ coverage data for devnode 9740 is shown in the following example:

```
|--------------------------------------------------------|
| MJ Device irp coverage                                 |
|--------------------------------------------------------|
| IRPS covered     12                      |  # of times |
|--------------------------------------------------------|
| IRP_MJ_UNKNOWN                           |           1 | 
| IRP_MJ_PNP                               |           6 | 
| IRP_MJ_DEVICE_CONTROL                    |           1 | 
| IRP_MJ_READ                              |           1 | 
| IRP_MJ_CREATE                            |           1 | 
| IRP_MJ_CLEANUP                           |           1 | 
| IRP_MJ_CLOSE                             |           1 | 
| IRP_MJ_WRITE                             |           1 | 
| IRP_MJ_SYSTEM_CONTROL                    |           3 | 
| IRP_MJ_FLUSH_BUFFERS                     |           1 | 
| IRP_MJ_POWER                             |           1 | 
| IRP_MJ_SHUTDOWN                          |           1 | 
|--------------------------------------------------------|
| IRPS NOT covered      1                  |             |
|--------------------------------------------------------|
| IRP_MJ_INTERNAL_DEVICE_CONTROL           |             | 
|--------------------------------------------------------|
| Stats                                                  |
|--------------------------------------------------------|
| Total IRP count        :     13                        |
| Covered IRP count      :     12                        |
| NOT Covered IRP count  :      1                        |
| Covered IRP %          :     92.31%                    |
| NOT Covered IRP %      :      7.69%                    |
|--------------------------------------------------------|
```

<span id="IRP_Pairs_Coverage_Data_______"></span><span id="irp_pairs_coverage_data_______"></span><span id="IRP_PAIRS_COVERAGE_DATA_______"></span>**IRP Pairs Coverage Data**   
This section shows the number of times a pair of IRPs were concurrently active within the devnode's driver stack during the IRP coverage period. The Driver Coverage toolkit monitors and reports on 1099 different IRP pairs.

This section shows the counters for each IRP MJ of MJ/MN function code that was concurrently processed by the driver. These counters can be used to determine which IRPs had adequate test coverage and which may need more coverage.

As with the other types of IRP coverage data, the data in this section can be used to analyze the efficiency of your code coverage tests. However, this data is significantly different since it shows how well the driver was tested for concurrent IRP processing.

The IRP pair coverage data for devnode 9740 is shown in the following example:

```
|--------------------------------------------------------|
| MJ & MN Device IRP Concurrency pairs.                  |
|--------------------------------------------------------|
| IRP Pairs covered                     25 |  # of times |
|--------------------------------------------------------|
| CREATE                                   |             | 
| READ                                     |          10 | 
|--------------------------------------------------------|
| CREATE                                   |             | 
| WRITE                                    |           5 | 
|--------------------------------------------------------|
| CREATE                                   |             | 
| DEVICE_CONTROL                           |           4 | 
|--------------------------------------------------------|
| CLOSE                                    |             | 
| READ                                     |          10 | 
|--------------------------------------------------------|
| CLOSE                                    |             | 
| WRITE                                    |           4 | 
|--------------------------------------------------------|
| CLOSE                                    |             | 
| DEVICE_CONTROL                           |           4 | 
|--------------------------------------------------------|
| READ                                     |             | 
| READ                                     |        1513 | 
|--------------------------------------------------------|
| READ                                     |             | 
| WRITE                                    |        1498 | 
|--------------------------------------------------------|
| READ                                     |             | 
| FLUSH_BUFFERS                            |         929 | 
|--------------------------------------------------------|
| READ                                     |             | 
| DEVICE_CONTROL                           |          68 | 
|--------------------------------------------------------|
| READ                                     |             | 
| CLEANUP                                  |          11 | 
|--------------------------------------------------------|
| READ                                     |             | 
| POWER\QUERY_POWER\SYSTEM                 |           1 | 
|--------------------------------------------------------|
| READ                                     |             | 
| WMI\QUERY_ALL_DATA                       |           2 | 
|--------------------------------------------------------|
| READ                                     |             | 
| PNP\QUERY_DEVICE_RELATIONS\Target        |           7 | 
|--------------------------------------------------------|
| READ                                     |             | 
| PNP\QUERY_PNP_DEVICE_STATE               |           1 | 
|--------------------------------------------------------|
| WRITE                                    |             | 
| WRITE                                    |        1448 | 
|--------------------------------------------------------|
| WRITE                                    |             | 
| FLUSH_BUFFERS                            |         852 | 
|--------------------------------------------------------|
| WRITE                                    |             | 
| DEVICE_CONTROL                           |           8 | 
|--------------------------------------------------------|
| WRITE                                    |             | 
| CLEANUP                                  |           4 | 
|--------------------------------------------------------|
| WRITE                                    |             | 
| PNP\QUERY_DEVICE_RELATIONS\Target        |           1 | 
|--------------------------------------------------------|
| WRITE                                    |             | 
| PNP\QUERY_PNP_DEVICE_STATE               |           2 | 
|--------------------------------------------------------|
| FLUSH_BUFFERS                            |             | 
| FLUSH_BUFFERS                            |          27 | 
|--------------------------------------------------------|
| FLUSH_BUFFERS                            |             | 
| DEVICE_CONTROL                           |           1 | 
|--------------------------------------------------------|
| DEVICE_CONTROL                           |             | 
| CLEANUP                                  |           7 | 
|--------------------------------------------------------|
| DEVICE_CONTROL                           |             | 
| PNP\START_DEVICE                         |           2 | 
|--------------------------------------------------------|
|--------------------------------------------------------|
| Stats                                                  |
|--------------------------------------------------------|
| Total IRP pairs                 :        1099          |
| Covered IRP pairs               :          25          |
| NOT Covered IRP pairs           :        1074          |
| Covered IRP pairs %             :           2.27%      |
| NOT Covered IRP pairs %         :          97.73%      |
|--------------------------------------------------------|
```

 

 





