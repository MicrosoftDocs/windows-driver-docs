---
title: Multiple DataSources
description: Multiple DataSources
ms.assetid: FD0B252F-1D70-4840-986F-94FF80D42246
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiple DataSources


Multiple DataSources are useful when you are looking for a combinatorial expansion of one or more DataSources ([Table based DataSource](table-data-source.md), [PICT based DataSource](pict-data-source.md), or [WMI based DataSource](wmi-data-source.md)).

Crafting your test design to make efficient use of this feature is paramount. Let's see with the aid of an example why this is so. Say as a part of multiple DataSource, you want to specify two Table based DataSources, one WMI based DataSource and one PICT Based DataSource. For the sake of argument, let's say that the first table has 4 rows, the second has 5 rows, the WMI query returns 2 results and the PICT DataSource generated 6 pairwise combinations. TAEF will come up with a combinatorial expansion of these sets of parameters. This means the test method in question will be invoked (4 X 5 X 2 X 6 =) **240** times! Increasing the number of invocations of the test method with varying combinations of parameters may yield diminishing results as far as test coverage goes. This makes it important to design the test using multiple DataSources with care and by weighing out other alternatives. Following are some points you may want to consider:

-   Make sure it adds value to have multiple tables. If you don't need them to be separate, you could come up with an efficient combination of parameters yourself.
-   Check if you can use a PICT model file with constraints, instead of multiple tables.
-   Check if there is value in refactoring your test case into multiple tests and associating subsets from the multiple DataSources with each newly created sub-test.

## <span id="Specify_multiple_DataSources"></span><span id="specify_multiple_datasources"></span><span id="SPECIFY_MULTIPLE_DATASOURCES"></span>Specify multiple DataSources


The key aspect here is how to specify the DataSource. Let's take a look at the code snippet from our native and managed examples.

### <span id="Native"></span><span id="native"></span><span id="NATIVE"></span>Native

```cpp
1   namespace WEX { namespace TestExecution { namespace Examples
2   {
3       class AdvancedDataDrivenTests
4       {
5           TEST_METHOD_SETUP(DataDrivenSetup);
6           TEST_METHOD_CLEANUP(DataDrivenCleanup);
7
8           TEST_CLASS(AdvancedDataDrivenTests)
9
10          BEGIN_TEST_METHOD(SecondTable)
11              TEST_METHOD_PROPERTY(L"DataSource", L"Table:AdvancedDataDrivenTests.xml#Table2;Table:CppTestLevelDataSource.xml#NestedTable")
12          END_TEST_METHOD()
13
14          BEGIN_TEST_METHOD(FirstTable)
15              TEST_METHOD_PROPERTY(L"DataSource", L"Table:AdvancedDataDrivenTests.xml#Table1;"
16                  L"PICT:PictDataSource.txt;" L"WMI:SELECT Location FROM Win32_StartupCommand")
17          END_TEST_METHOD()
18      };
19  } /* namespace Examples */ } /* namespace TestExecution */ } /* namespace WEX */
```

See lines 11, 15, and 16 in the example above. In general, the pattern to follow to specify the DataSource is a semi-colon separated list of each DataSource specification. The specification would look very similar in managed code as well.

### <span id="Managed"></span><span id="managed"></span><span id="MANAGED"></span>Managed

```cpp
[TestMethod]
[DataSource(@"Table:CSharpAdvancedDataDrivenTests.xml#FirstTable;
    WMI:SELECT ProcessId FROM Win32_Service WHERE Name=&#39;Themes&#39;")]

public void First()
{
    Log.Comment("In CSharpAdvancedDataDrivenTests.First");
    String[] shapes = m_testContext.DataRow["Shape"] as String[];
    foreach (String shape in shapes)
    {
        Console.WriteLine("The shape is " + shape);
    }

    Int32[] lengths = m_testContext.DataRow["Length"] as Int32[];
    foreach (int length in lengths)
    {
        Console.WriteLine("The length is " + length.ToString());
    }

    String description = (String)m_testContext.DataRow["Description"];
    Boolean desktopInteract = (Boolean)m_testContext.DataRow["DesktopInteract"];
    UInt32 processId = (UInt32)m_testContext.DataRow["ProcessId"];
    Log.Comment("Themes service is running on process " + processId.ToString());
    Log.Comment("Themes service description: " + description);
}
```

The examples also demonstrate the ways to specify multiple DataSources in multiple lines. Of course, you could have specified the DataSource on a single line (as shown below), but you could improve readability significantly by using the above shown constructs.

## <span id="Specifying_DataSource_on_a_single_line"></span><span id="specifying_datasource_on_a_single_line"></span><span id="SPECIFYING_DATASOURCE_ON_A_SINGLE_LINE"></span>Specifying DataSource on a single line


```cpp
[DataSource("Table:CSharpAdvancedDataDrivenTests.xml#FirstTable;WMI:SELECT ProcessId FROM Win32_Service WHERE Name=&#39;Themes&#39;")]
```

Just to re-iterate: **the test method will be run once for each n-way combinatorial expansion of data sets generated by each individual DataSource**. For example, for the above managed example, safely assuming that there is only one Themes service running, and knowing that there are 3 Rows in the table data source provided, the test method will be invoked 3 times (1 X 3). In the native example case, in SecondTable test method, there are two table DataSources specified. The first table contains 3 Rows and the second table contains 4 rows. Hence the test method will be invoked 12 times (3 X 4).

## <span id="Constraints_that_apply_while_specifying_Multiple_DataSources"></span><span id="constraints_that_apply_while_specifying_multiple_datasources"></span><span id="CONSTRAINTS_THAT_APPLY_WHILE_SPECIFYING_MULTIPLE_DATASOURCES"></span>Constraints that apply while specifying Multiple DataSources


The constraints are applicable only when you want to specify a Table based DataSource in the multiple DataSource specifications. **Table DataSource** must be specified as Table:&lt;reative path to XML file&gt;\#&lt;TableId&gt;. If TAEF discovers that "TableId" is provided as a separate metadata, it will assume that the DataSource is a single Table-based DataSource and proceed.

 

 





