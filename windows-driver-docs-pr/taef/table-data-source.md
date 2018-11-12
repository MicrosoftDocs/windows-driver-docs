---
title: Table Data Source
description: Table Data Source
ms.assetid: D0CC0536-5569-47ed-8DE8-B64FF3042C51
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Table Data Source


Please make sure that you are familiar with basic execution of [TAEF](index.md) and know how to [Author Tests](authoring-tests.md) using it, before proceeding with this section.

Now that you have basic test automation written and working with TAEF, you can concentrate on scenarios where the same test code can be used to work on varying sets of data. For this purpose, TAEF provides a "Table based" approach to data driven tests. Let's take a look at a simple example to understand how to go about authoring a data driven test.

Consider a simple non-data driven example in which you are printing the size and theme to the console. In this exercise, you will convert this test to a data driven test.

```cpp
1  namespace WEX { namespace TestExecution { namespace Examples
2  {
3     void DataDrivenTests::FirstTable()
4     {
5         int size = 12;
6         Log::Comment(String().Format(L"Size retrieved was %d", size));
7     }
8
9     void DataDrivenTests::SecondTable()
10    {
11        String theme = "Aero";
12        Log::Comment(L"Theme supplied as " + theme);
13    }
14 } /* namespace Examples */ } /* namespace TestExecution */ } /* namespace WEX */
```

## <span id="Defining_the_Data"></span><span id="defining_the_data"></span><span id="DEFINING_THE_DATA"></span>Defining the Data


Now, you want the function above to work for a set of sizes and themes. In other words, you want variant data values that our function can consume. In order to do this, define two tables in an XML file DataDrivenTests.xml :

```cpp
1  <?xml version="1.0"?>
2  <Data>
3  <Table Id ="Table1">
4          <ParameterTypes>
5                  <ParameterType Name="Size">Int32</ParameterType>
6                  <ParameterType Name="Color">String</ParameterType>
7                  <ParameterType Name="Transparency">Boolean</ParameterType>
8          </ParameterTypes>
9          <Row Priority="1" Owner="C2">
10                 <Parameter Name="Size">12</Parameter>
11                 <Parameter Name="Color">Blue</Parameter>
12                 <Parameter Name="Transparency">True</Parameter>
13         </Row>
14         <Row Priority="2" Owner="wex">
15                 <Parameter Name="Size">4</Parameter>
16                 <Parameter Name="Color">White</Parameter>
17                 <Parameter Name="Transparency">False</Parameter>
18         </Row>
19         <Row Owner="C2">
20                 <Parameter Name="Size">9</Parameter>
21                 <Parameter Name="Color">Black</Parameter>
22                 <Parameter Name="Transparency">True</Parameter>
23         </Row>
24 </Table>
25 <Table id ="Table2">
26         <Row Description="ButtonTest" Owner="C2" Priority="1">
27                 <Parameter Name="Control">Button</Parameter>
28                 <Parameter Name="Theme">Aero</Parameter>
29         </Row>
30         <Row Description="ComboBoxTest" Priority="2">
31                 <Parameter Name="Control">ComboBox</Parameter>
32                 <Parameter Name="Theme">Classic</Parameter>
33         </Row>
34         <Row Description="ListviewTest" Owner="wex">
35                 <Parameter Name="Control">Listview</Parameter>
36                 <Parameter Name="Theme">AeroBasic</Parameter>
37         </Row>
38 </Table>
39 </Data>
```

You have now defined two tables, "Table1" and "Table2". **You may define tables for several test methods in the same XML file.**

Observe that in Table1, you defined the ParameterTypes up front and chose "Size" to be an integer. **The ParameterTypes section is optional.** By default, if parameter type information is not provided, it will be saved as a string. This is the case for all the parameters in "Table2".

Each "Row" defined within a table is a set of data (parameter) values that you would like the test function to accept. Lines 9, 14 and 19 define 3 sets of data that our FirstTable function would accept. Similarly lines 26, 30 and 34 define the data sets for SecondTable.

Notice lines 9, 14, 19, 26, 30, and 34 in the example above - you can define metadata that is specific to the Row. There is now a way for metadata information to change with data sets for the same function. The priority for the first set of data (line 9) is 1, priority for second set of data (line 14) is 2 and the third set of data (line 19) defaults to the priority of the function. **All the rows inherit the metadata from the function the table is associated with. If the same metadata is specified again at the row level, it will override the metadata values defined at the function level.**

**NOTE: The XML file schema definition is the same for native as well as managed code, except for type definitions supported.** See initial part of "Managed Data Driven Test" section below for another example of how to define the data. Continue with Native Data Driven Test to understand types allowed in native code.

## <span id="Native_Data_driven_test"></span><span id="native_data_driven_test"></span><span id="NATIVE_DATA_DRIVEN_TEST"></span>Native Data driven test


With the data sets defined and ready for consumption, you now need a way to qualify the test function as a data driven test and associate it with the table that defines the data set. This is done by way of extra metadata while authoring the test:

```cpp
1  namespace WEX { namespace TestExecution { namespace Examples
2  {
3      class DataDrivenTests
4      {
5          TEST_CLASS(DataDrivenTests);
6
7          BEGIN_TEST_METHOD(SecondTable)
8              TEST_METHOD_PROPERTY(L"DataSource", L"Table:DataDrivenTests.xml#Table2")
9              TEST_METHOD_PROPERTY(L"Priority", L"3")
10         END_TEST_METHOD()
11
12         BEGIN_TEST_METHOD(FirstTable)
13             TEST_METHOD_PROPERTY(L"Priority", L"4")
14             TEST_METHOD_PROPERTY(L"DataSource", L"Table:DataDrivenTests.xml#Table1")
15         END_TEST_METHOD()
16     };
17 } /* namespace Examples */ } /* namespace TestExecution */ } /* namespace WEX */
```

In order to associate the XML Table with the test, add the 'DataSource' metadata to the test's method. Through this association TAEF will use the given DataSource to drive the test. The DataSource value has three parts to it:

1.  'Table:' - this identifies the data source as being an XML table.
2.  'DataDrivenTests.xml' - this is the file that contains the XML table.
3.  '\#Table2' - Following the '\#' delimeter, the 'Table2' value identifies the particular table within the XML document to use. A single XML Table data source can contain multiple tables. TAEF will look through the XML file for a Table element with an 'Id' attribute that matches the specified value.

You may have observed in the above example that "SecondTable" is defined before "FirstTable". This means that "SecondTable" function will get executed before the "FirstTable" function, but you defined "Table1", the table corresponding to "FirstTable", before "Table2", the table corresponding to "SecondTable". This is to emphasize that **the order of table definition is irrelevant during the discovery and execution of the data driven tests.**

With the mapping of our data source to the test method complete, you can now modify the example to get the data from the source. Before doing that, take a look at the published header file, TestData.h. The part of interest is:

```cpp
1    class TestData
2    {
3    public:
4        template <typename T>
5        static HRESULT __stdcall TryGetValue(_In_z_ const wchar_t* pszString, T& result)
6        {
7            return Private::TestData<T>::TryGetValue(pszString, result);
8        }
9    };
```

Line 5 shows the API to call in order to retrieve the data in the function. Take a look at the available [Parameter Types](parameter-types-in-table-data-sources.md) for retrieval.

Ok - all set to re-write our example:

```cpp
1  namespace WEX { namespace TestExecution { namespace Examples
2  {
3      void DataDrivenTests::FirstTable()
4      {
5          Log::Comment(L"I am in first table");
6          int size;
7          if (SUCCEEDED(TestData::TryGetValue(L"size", size)))
8          {
9              VERIFY_ARE_NOT_EQUAL(size, 0);
10             Log::Comment(String().Format(L"Size retrieved was %d", size));
11         }
12     }
13
14     void DataDrivenTests::SecondTable()
15     {
16         Log::Comment(L"I am in second table.");
17         String theme;
18         if (SUCCEEDED(TestData::TryGetValue(L"theme", theme)))
19         {
20             Log::Comment(L"Theme supplied as " + theme);
21         }
22     }
23 } /* namespace Examples */ } /* namespace TestExecution */ } /* namespace WEX */
```

Lines 7 and 18 are the main parts that changed in order to make the test data driven. Not a great deal of change. Take a look at Executing Data Driven Tests to understand how to make the most of TAEF while executing data driven tests.

## <span id="Managed_Data_driven_test"></span><span id="managed_data_driven_test"></span><span id="MANAGED_DATA_DRIVEN_TEST"></span>Managed Data driven test


Consider an example where you want to print the co-ordinates of a rectangle on the console. Start with defining these co-ordinates as the data set in an XML file.

```cpp
1  <?xml version="1.0"?>
2  <Data>
3  <Table Id="FirstTable">
4          <ParameterTypes>
5                  <ParameterType Name="Left">Int32</ParameterType>
6                  <ParameterType Name="Right">String</ParameterType>
7                  <ParameterType Name="Top">Integer</ParameterType>
8                  <ParameterType Name="Bottom">Int32</ParameterType>
9          </ParameterTypes>
10         <Row Priority="1" Owner="C2" Description="Zero rect">
11                 <Parameter Name="Left">0</Parameter>
12                 <Parameter Name="Right">0</Parameter>
13                 <Parameter Name="Top">0</Parameter>
14                 <Parameter Name="Bottom">0</Parameter>
15         </Row>
16         <Row Priority="2" Owner="wex" Description="normal rect">
17                 <Parameter Name="Left">12</Parameter>
18                 <Parameter Name="Right">25</Parameter>
19                 <Parameter Name="Top">10</Parameter>
20                 <Parameter Name="Bottom">50</Parameter>
21         </Row>
22         <Row Owner="C2" Description="invalid rect">
23                 <Parameter Name="Left">30</Parameter>
24                 <Parameter Name="Right">15</Parameter>
25                 <Parameter Name="Top">40</Parameter>
26                 <Parameter Name="Bottom">10</Parameter>
27         </Row>
28 </Table>
29 </Data>
```

Define the data set in the scope of a Table, in this case "FirstTable", which is defined in line 3 above. **You may define tables for several test methods in the same XML file.**

Observe that FirstTable defines the ParameterTypes upfront and calls out "Left" to be an "Int32". **The ParameterTypes section is optional. By default, if parameter type information is not provided, it will be saved as a String.**

Take a look at the list of supported [Parameter Types](parameter-types-in-table-data-sources.md).

If any other data type is specified, the test will throw a warning and consider it to be a String.

**NOTE: The type strings are case insensitive but should spell exactly as shown above.**

Each "Row" defined within a table, is a set of data (parameter) values that you would like the test function to accept. Lines 10, 16 and 22 define 3 sets of data that our function.

Notice lines 10, 16, and 22 in the example above - you can define metadata specific to Row. You now have a way for metadata information to change with data sets for the same function. The priority for the first set of data (line 10) is 1, priority for second set of data (line 16) is 2 and the third set of data (line 22) defaults to the priority of the function. **All the rows inherit the metadata from the function the table is associated with. If the same metadata is specified again at the row level, it will override the metadata values defined at the function level.**

**NOTE: The XML file schema definition is the same for native as well as managed code, except for type definitions supported.** Take a look at "Defining the Data" section at the top of this page for another example of how to define this.

Now, you have all the data defined. The following example shows how to access it.

```cpp
1  namespace WEX.Examples
2  {
3      using Microsoft.VisualStudio.TestTools.UnitTesting;
4      using System;
5      using System.Collections;
6      using WEX.Logging.Interop;
7      using WEX.TestExecution;
8
9      [TestClass]
10     public class CSharpDataDrivenTests
11     {
12         [TestMethod]
15         [DataSource("Table:CSharpDataDrivenTests.xml#FirstTable")]
16         public void First()
17         {
18             Console.WriteLine("Left is " + m_testContext.DataRow["Left"].ToString());
19
20             Log.Comment("In CSharpDataDrivenTests.First");
21         }
22
23         [TestMethod]
24         public void Second()
25         {
26             Log.Comment("In CSharpDataDrivenTests.Second");
27             Verify.IsTrue(true);
28         }
29
30         public TestContext TestContext
31         {
32             get { return m_testContext; }
33             set { m_testContext = value; }
34         }
35
36         private TestContext m_testContext;
37     }
38 }
```

Associating the XML Table with a given test method in managed code is very similar to native code; simply apply the 'DataSource' metadata. As before, it's comprised of three parts:

1.  'Table:' - to identify the data source as being an XML table.
2.  'CSharpDataDrivenTests.xml' - the file that contains the XML table.
3.  '\#FirstTable' - Following the '\#' delimeter, the 'FirstTable' value identifies the particular table within the XML document to use. TAEF will look through the XML file for a Table element with an 'Id' attribute that matches the specified value.

Notice that the Second function is not data-driven. **You may choose to have only some of your tests to be data driven. You also have the option of having each test have its table defined in a different XML file.**

In Line 36, you define a private TestContext property - like VSTS recommends (<https://msdn2.microsoft.com/library/ms404699(VS.80).aspx>). You also define public assessors to this property (lines 30 through 34). Internally TAEF loads the dictionary property of TestContext with the corresponding data set in focus.

TestContext is defined in Microsoft.VisualStudio.TestTools.UnitTesting. See line 3 in the example above. You should already be including this as a reference in your managed test authoring. **So, no additional references are required for authoring data driven tests.**

In line 18 of the example above, you show how to retrieve data in the function. Notice that the data is available in m\_testContext.DataRow.

## <span id="Name_instead_of_Index_to_Identify_a_DataRow"></span><span id="name_instead_of_index_to_identify_a_datarow"></span><span id="NAME_INSTEAD_OF_INDEX_TO_IDENTIFY_A_DATAROW"></span>Name instead of Index to Identify a DataRow


TAEF allows you to have a more meaningful 'Name' property instead of the Index to identify any DataRow in your DataSource. To do this, simply add 'Name' metadata at the Row level in your DataSource. Our first example on this page can be modified to use this feature as follows:

```cpp
1  <?xml version="1.0"?>
2  <Data>
3  <Table id ="Table1">
4          <ParameterTypes>
5                  <ParameterType Name="Size">Int32</ParameterType>
6                  <ParameterType Name="Color">String</ParameterType>
7                  <ParameterType Name="Transparency">Boolean</ParameterType>
8          </ParameterTypes>
9          <Row Name=&#39;BlueTransparent&#39; Priority="1" Owner="C2">
10                 <Parameter Name="Size">12</Parameter>
11                 <Parameter Name="Color">Blue</Parameter>
12                 <Parameter Name="Transparency">True</Parameter>
13         </Row>
14         <Row Priority="2" Owner="wex">
15                 <Parameter Name="Size">4</Parameter>
16                 <Parameter Name="Color">White</Parameter>
17                 <Parameter Name="Transparency">False</Parameter>
18         </Row>
19         <Row Name=&#39;BlackTransparent&#39; Owner="C2">
20                 <Parameter Name="Size">9</Parameter>
21                 <Parameter Name="Color">Black</Parameter>
22                 <Parameter Name="Transparency">True</Parameter>
23         </Row>
24 </Table>
25 ...
39 </Data>
```

In the above modified example, 'BlueTransparent' correspondes to index 0. The Row with index 1 has no special name given to it and the Row with index 2 has the Name 'BlackTransparent associated with it. You can still use a selection query to look for index 0 or 2 in 'Table1', and it will find the correct Row. But, when executing or listing the dll, instead of seeing:

```cpp
<qualified name of the test method>#<index>
```

you will instead see:

```cpp
<qualified name of the test method>#<name property provided at Row level>
```

for the Rows where "Name" attribute is provided at the Row level. If the "Name" property is not provided for any Row, like in the case of index 1 above, it will default to having \#**&lt;index&gt;** at the method's qualified name.

NOTE that by way of providing a "Name" attribute at Row level, you are essentially changing the way TAEF interprets the name of the instance of the method invocation with the corresponding Row data.

## <span id="DataSource_as_a_Runtime_parameter"></span><span id="datasource_as_a_runtime_parameter"></span><span id="DATASOURCE_AS_A_RUNTIME_PARAMETER"></span>DataSource as a Runtime parameter


TAEF supports supplying the datasource as a runtime parameter. The syntax for this is as follows:

```cpp
te <test dll names> /p:<DataSource runtime name>=Table:<DataSoure XML file>#<Table Id>
```

While authoring the test in concern, you must specify the "p:&lt;DataSource runtime name&gt;" as your Data Source. Keep in mind that you have to specify the complete string - the XML file name as well as the table id together - at runtime. The TableId is not expected to be provided as a test metadata if your datasource is provided at runtime. The "Table:" prefix specifies that you are looking for a table data source.

You can try this out with one of the examples available on the release share:

``` syntax
te Examples\CPP.RuntimeDataSource.Example.dll /p:MyDataSource=Table:RuntimeDataSourceExample.xml#SimpleTable
```

## <span id="DataSource_as_a_Resource"></span><span id="datasource_as_a_resource"></span><span id="DATASOURCE_AS_A_RESOURCE"></span>DataSource as a Resource


TAEF allows you to add your DataSource as a resource of your test module as long as it conforms with the following:

In case of native test modules, you can do this by specifying your DataSource as the resource id or resource name. Here is a code example:

```cpp
BEGIN_TEST_METHOD(ResourceNameDataSource)
    TEST_METHOD_PROPERTY(L"DataSource", L"Table:MyResourceName#SimpleTable")
END_TEST_METHOD()
```

"MyResourceName" is the resource name as is defined in ResourceDataSource.rc file in this case:

```cpp
MyResourceName DATASOURCE_XML "ResourceDataSource.xml"
```

In case of managed test modules, the resource can only be specified in a certain way as shown in the **sources** file snippet shown below:

```cpp
LANGUAGE_NEUTRAL_MANAGED_RESOURCES = CSharpAdvancedDataDrivenTests.xml
```

The DataSource metadata specification will remain the same as it did in case of specifying the DataSource XML file. Similar to the case in managed code, you could make the resource name the same as the XML file name. It is hence, important to understand that TAEF will first look for the presence of the actual file with the DataSource name. If such an XML file is not found, only then will it proceed with looking for test resource in the test module with the given resource name or id. Since specifying the DataSource as a resource requires re-compiling, you can take advantage of this design by copying over the DataSource XML file to the same location as the test dll while developing (and naming the resource name to be the same as the XML file name). Once you are done testing, copy the XML back to the code directory and re-compile as a resource. Don't forget to delete the XML file from the execution directory! :)

## <span id="Example_Walk-throughs"></span><span id="example_walk-throughs"></span><span id="EXAMPLE_WALK-THROUGHS"></span>Example Walk-throughs


To grasp various aspects of table based data-driven testing, take a read of some more example walk-throughs:

-   [Simple Data Driven Example](data-driven-testing.md)
-   [Overriding metadata at the Row level](metadata-overriding-data-driven-test-example.md)
-   [Specifying array parameter types](array-support-data-driven-test-example.md)
-   [Data-driven Class](data-driven-class.md)

 

 





