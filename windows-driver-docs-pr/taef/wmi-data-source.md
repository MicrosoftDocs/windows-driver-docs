---
title: WMI Data Source
description: WMI Data Source
ms.assetid: 1C9D0EEC-6542-4249-B7E0-CA3ED63FB120
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WMI Data Source


Please make sure that you are familiar with basic execution of TAEF and know how to Author Tests using it, before proceeding with this section.

## <span id="Background"></span><span id="background"></span><span id="BACKGROUND"></span>Background


"WMI" stands for "Windows Management Instrumentation". Using the Common Information Model (CIM), which is the industry standard to represent systems. Windows Management Instrumentation provides a unified way for accessing system management information.

## <span id="How_does_it_help_my_tests_"></span><span id="how_does_it_help_my_tests_"></span><span id="HOW_DOES_IT_HELP_MY_TESTS_"></span>How does it help my tests?


Using the WMI query support available as the WMI DataSource in TAEF, you can add a precondition to your test as well as get information about the resources on the test machine before running your test. Here are some of the examples of the kind of query you could make using WMI:

-   Check if the machine the test is running on is a laptop and run the test only if it is a laptop.
-   Check if a service pack has been installed on the test machine and run the test only if it has been.
-   Retrieve all the removable drives and local hard disk drives on the test machine and run the test for each of the drives that match the query.
-   Run the test only if the test machine is not domain joined OR
-   Run the test only if the test machine is domain joined and retrieve the domain name.

That would have hopefully given you some idea on where and how you can leverage WMI DataSource for your testing. Let's look at how to add this WMI query support while authoring a TAEF test.

The only special metadata you need to make your test a WMI DataSource test is the "DataSource". The DataSource syntax must look as follows:

```cpp
[DataSource("WMI:<WQL query>")]
```

Or in native code:

```cpp
TEST_METHOD_PROPERTY(L"DataSource", L"WMI:<WQL query>")]
```

You must have noticed that the DataSource value starts with "WMI:" which lets TAEF know that this is indeed the data source for a test that depends on WMI query result and also distinguishes it from data-driven test. This is good opportunity to mention that currently TAEF does not support a test to be both - a data-driven test as well as a test that depends on the WMI query result.

The next question naturally is how to write WQL queries for what you are looking for? WQL query syntax is very similar to simplified SQL queries. There are some very good examples of queries provided on [https://msdn2.microsoft.com/library/aa394585(VS.85).aspx.](https://msdn2.microsoft.com/library/aa394585(VS.85).aspx) Here are a few examples:

<span id="SELECT_Description__DesktopInteract__ProcessId_FROM_Win32_Service_WHERE_Name__Themes_"></span><span id="select_description__desktopinteract__processid_from_win32_service_where_name__themes_"></span><span id="SELECT_DESCRIPTION__DESKTOPINTERACT__PROCESSID_FROM_WIN32_SERVICE_WHERE_NAME__THEMES_"></span>SELECT Description, DesktopInteract, ProcessId FROM Win32\_Service WHERE Name='Themes'  
Run the test on the "Themes" service after finding out it's Description, DesktopInteract and ProcessId properties which you intend to use in your testing.

<span id="SELECT_Capabilities__CapabilityDescriptions_FROM_Win32_Printe"></span><span id="select_capabilities__capabilitydescriptions_from_win32_printe"></span><span id="SELECT_CAPABILITIES__CAPABILITYDESCRIPTIONS_FROM_WIN32_PRINTE"></span>SELECT Capabilities, CapabilityDescriptions FROM Win32\_Printe  
Run the test for each printer connected to this computer. Allow the test to access the Capabilities and CapabilityDescriptions for each printer.

<span id="SELECT_Name__User__Location_FROM_Win32_StartupCommand"></span><span id="select_name__user__location_from_win32_startupcommand"></span><span id="SELECT_NAME__USER__LOCATION_FROM_WIN32_STARTUPCOMMAND"></span>SELECT Name, User, Location FROM Win32\_StartupCommand  
Run the test for each process that gets run at Windows startup. For each process let the test know what the Name of the process is, where it is located (Location), and what User the process runs as.

You can find more examples in the documentation mentioned above as well as in the .cs file and header file in the examples you have opened. The general, over-simplified syntax is as follows:

```cpp
SELECT <comma separated properties> FROM <WMI Class name> [WHERE <add condition on some properties>]
```

In the examples that you just saw, Win32\_Service, Win32\_Printer and Win32\_StartupCommand are all WMI Classes. You can look up what WMI class you are interested in for your test here: [https://msdn2.microsoft.com/library/aa394554(VS.85).aspx.](https://msdn2.microsoft.com/library/aa394554(VS.85).aspx)

TAEF does not support retrieving System Properties.

Behind the scene TAEF will execute the query for you and confirm the result. If at least one object is returned as a result of the query, the test gets executed for each returned object. If the WQL query does not return any objects, the test gets logged as Blocked with this information and execution moves on to the next test.

Checking or verifying your query before authoring your test seems to be a great idea, and is a very simple process:

-   Either from the run dialog or a command prompt invoke "wbemtest.exe"
-   Click the "Connect" button on the upper right corner.
-   Make sure your namespace is "root\\cimv2" before clicking "Connect" again on the upper right corner.
-   Under "IWbemServices", click "Query"
-   Enter your query in the edit box that appears and click "Apply"

NOTE: The "IWbemService" have several other options that could help you with your query. For example, using "Enum Classes" and changing the radio button to "recursive" will help you see all the WMI classes on the system.

## <span id="Retrieving_properties_queried_using_the_WMI_query"></span><span id="retrieving_properties_queried_using_the_wmi_query"></span><span id="RETRIEVING_PROPERTIES_QUERIED_USING_THE_WMI_QUERY"></span>Retrieving properties queried using the WMI query


By now you have an idea of how to come up with a WMI query for a test method and how to apply it as a metadata while authoring a test. You also know how to confirm that the query is valid using wbemtest.exe. Now let's look at how to retrieve the property values that you were looking for.

The basics on retrieving this information are very similar to retrieving values for your data-driven test. For example, in managed code this would look as follows:

```cpp
1 namespace WEX.Examples
2 {
3     using Microsoft.VisualStudio.TestTools.UnitTesting;
4     using System;
5     using System.Collections;
6     using System.Data;
7     using WEX.Logging.Interop;
8     using WEX.TestExecution;
9
10    [TestClass]
11    public class CSharpWmiDataSourceExample
12    {
13        [TestMethod]
14        [DataSource("WMI:SELECT Description, DesktopInteract, ProcessId FROM Win32_Service WHERE Name=&#39;Themes&#39;")]
15        public void ThemesTest()
16        {
17            String description = (String)m_testContext.DataRow["Description"];
18            Boolean desktopInteract = (Boolean)m_testContext.DataRow["DesktopInteract"];
19            UInt32 processId = (UInt32)m_testContext.DataRow["ProcessId"];
20            Log.Comment("Themes service is running on process " + processId.ToString() + " with desktop interact set to "
                           + desktopInteract.ToString());
21            Log.Comment("Themes service description: " + description);
22        }
23        ...
24        public TestContext TestContext
25        {
26            get { return m_testContext; }
27            set { m_testContext = value; }
28        }
29
30        private TestContext m_testContext;
31    }
32}
```

Lines 24-30 in the example above are exactly what is required for a managed data-driven test. You defined a private TestContext property and provided public getter and setter on it for TAEF to set the right values. Using the private TestContext property, you can retrieve the current value for any of the WMI query resultant object's properties that you retrieved from TAEF.

The native code for retrieving the WMI properties is very similar. Like with native data-driven tests, you will use TestData to get the property values. For example, let's consider the test for getting properties of the default printer. The header file authors this test like so:

```cpp
1        // Test on the default printer and its driver name
2        BEGIN_TEST_METHOD(DefaultPrinterTest)
3            TEST_METHOD_PROPERTY(L"DataSource",
              L"WMI:SELECT DriverName, DeviceId, LanguagesSupported FROM Win32_Printer WHERE Default = True")
4        END_TEST_METHOD()
```

For this, our retrieval code, in the cpp file looks as follows:

```cpp
1     void WmiExample::DefaultPrinterTest()
2     {
3         String deviceId;
4         VERIFY_SUCCEEDED(TestData::TryGetValue(L"DeviceId", deviceId));
5
6         String driverName;
7         VERIFY_SUCCEEDED(TestData::TryGetValue(L"DriverName", driverName));
8
9         TestDataArray<unsigned int> languagesSupported;
10        VERIFY_SUCCEEDED(TestData::TryGetValue(L"LanguagesSupported", languagesSupported));
11
12        Log::Comment(L"The default driver is " + deviceId + L" which is a " + driverName);
13        size_t count = languagesSupported.GetSize();
14        for (size_t i = 0; i < count; i++)
15        {
16            Log::Comment(String().Format(L"Language supported: %d", languagesSupported[i]));
17        }
18    }
```

## <span id="Accounting_for_possible_NULL_property_values"></span><span id="accounting_for_possible_null_property_values"></span><span id="ACCOUNTING_FOR_POSSIBLE_NULL_PROPERTY_VALUES"></span>Accounting for possible NULL property values


The part to keep in mind is that the WMI query may not always return a non-null property. There could be times when the WMI property value returned is "null". If you think the property that you are looking for could be "null" in some scenarios, then check for it before verifying or trying to use it.

In managed test code for example, TestContext will store the null values as an object of type DBNull. You must check if the object is of type DBNull before trying to cast the resultant value to the type you expect it to be. Let's take a look:

```cpp
1 namespace WEX.Examples
2 {
3     using Microsoft.VisualStudio.TestTools.UnitTesting;
4     using System;
5     using System.Collections;
6     using System.Data;
7     using WEX.Logging.Interop;
8     using WEX.TestExecution;
9
10    [TestClass]
11    public class CSharpWmiDataSourceExample
12    {
13        [TestMethod]
14        [DataSource("WMI:SELECT MaximumComponentLength, Availability, DeviceId, DriveType, Compressed
                         FROM Win32_LogicalDisk WHERE DriveType=2 Or DriveType=3")]
15        public void LogicalDiskTest()
16        {
17            UInt32 driveType = (UInt32)m_testContext.DataRow["DriveType"];
18            Log.Comment("DeviceId is " + m_testContext.DataRow["DeviceId"]);
19            Log.Comment("DriveType is " + driveType.ToString());
20
21            object nullCheckCompressed = m_testContext.DataRow["Compressed"];
22            Log.Comment("Compressed&#39;s type is: " + nullCheckCompressed.GetType().ToString());
23            if (nullCheckCompressed.GetType() == typeof(DBNull))
24            {
25                Log.Comment("Compressed is NULL");
26            }
27            else
28            {
29                Boolean compressed = (Boolean)nullCheckCompressed;
30                Log.Comment("Compressed is " + compressed.ToString());
31            }
32
33            object nullCheckMaxComponentLength = m_testContext.DataRow["MaximumComponentLength"];
34            if (nullCheckMaxComponentLength.GetType() == typeof(DBNull))
35            {
36                Log.Comment("MaxComponentLength is NULL");
37            }
38            else
39            {
40                UInt32 maxComponentLength = (UInt32)nullCheckMaxComponentLength;
41                Log.Comment("MaxComponentLength is " + maxComponentLength.ToString());
42            }
43
44            object nullCheckAvailability = m_testContext.DataRow["Availability"];
45            if (nullCheckAvailability.GetType() == typeof(DBNull))
46            {
47                Log.Comment("Availability is NULL");
48            }
49            else
50            {
51                UInt32 availability = (UInt32)nullCheckAvailability;
52                Log.Comment("Availability is " + availability.ToString());
53            }
54        }
55        ...
56        public TestContext TestContext
57        {
58            get { return m_testContext; }
59            set { m_testContext = value; }
60        }
61
62        private TestContext m_testContext;
63    }
64}
```

For example, in the above test, "Compressed", "MaximumComponentLength" and "Availability" can be null in some scenarios (when the query returns removable drives like floppy drives). You want to make sure that the test behaves appropriately in such cases. Toward this end, retrieve the property value as an object and check if it is of type "DBNull". If it is, it means that the property value returned was null. If it is not, the value returned was not null and hence valid - so cast it to the appropriate types and use it for the testing.

The same is true with native retrievals APIs as well - the property value returned could be NULL. This means that you need to check if the TestData successfully retrieved the value without using a verify call (since not being able to retrieve could be because the value is null). For example, you may have a test method that depends on a WMI query:

```cpp
1        // Test on only local (drive type = 3) or removable (drive type = 2) harddrive
2        BEGIN_TEST_METHOD(LocalOrRemovableHardDriveTest)
3            TEST_METHOD_PROPERTY(L"DataSource", L"WMI:SELECT DeviceId, DriveType, Availability,
                  MaximumComponentLength FROM Win32_LogicalDisk WHERE DriveType=2 OR DriveType=3")
4        END_TEST_METHOD()
```

You may have "Availability and "MaximumComponentLength" returned as NULL values. So write the test to account for this like so:

```cpp
1     void WmiExample::LocalOrRemovableHardDriveTest()
2     {
3         String deviceId;
4         VERIFY_SUCCEEDED(TestData::TryGetValue(L"DeviceId", deviceId));
5         int driveType;
6         VERIFY_SUCCEEDED(TestData::TryGetValue(L"DriveType", driveType));
7
8         unsigned int maxComponentLength;
9         if (SUCCEEDED(TestData::TryGetValue(L"MaximumComponentLength", maxComponentLength)))
10        {
11            Log::Comment(String().Format(L"MaximumComponentLength: %d", maxComponentLength));
12        }
13
14        unsigned int availability;
15        if (SUCCEEDED(TestData::TryGetValue(L"Availability", availability)))
16        {
17            Log::Comment(String().Format(L"Availability: %d", availability));
18        }
19
20        Log::Comment(L"DeviceId: " + deviceId);
21        Log::Comment(String().Format(L"DriveType: %d", driveType));
22    }
```

 

 





