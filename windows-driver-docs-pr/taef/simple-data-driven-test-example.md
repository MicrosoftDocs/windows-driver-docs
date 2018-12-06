---
title: Simple Data Driven Test Example
description: Simple Data Driven Test Example
ms.assetid: 59A897C3-C9CD-4e1c-B4BA-F81B3B3E4532
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Simple Data Driven Test Example


This section describes several examples of data driven testing and covers specific features in each example.

The first example, is a basic data driven test, called SimpleDataDrivenExample.

In the managed example, you will find an XML file which looks like this:

```cpp
    1  <?xml version="1.0"?>
    2  <Data>
    3    <Table Id="Table1">
    4      <ParameterTypes>
    5        <ParameterType Name="Size">Int32</ParameterType>
    6        <ParameterType Name="Color">String</ParameterType>
    7      </ParameterTypes>
    8      <Row>
    9        <Parameter Name="Size">4</Parameter>
    10       <Parameter Name="Color">White</Parameter>
    11     </Row>
    12     <Row>
    13       <Parameter Name="Size">10</Parameter>
    14       <Parameter Name="Color">Black</Parameter>
    15     </Row>
    16     <Row>
    17       <Parameter Name="Size">9</Parameter>
    18       <Parameter Name="Color">Orange</Parameter>
    19     </Row>
    20     <Row>
    21       <Parameter Name="Size">9</Parameter>
    22       <Parameter Name="Color">Blue</Parameter>
    23     </Row>
    24   </Table>
    25 </Data>
```

This XML file defines the data parameters for our data driven test to consume. The top XML node is the **&lt;Data&gt;** tag, which may contain **one or more &lt;Table&gt;** tags defined within it. **Every table needs to be associated with a unique "ID" attribute.** The test functions use the table ID value to identify the particular Table that they will use in the XML file.

Within the &lt;Table&gt; tag, you have an optional **&lt;ParameterTypes&gt;** section. Here you can explicitly specify the data type for a given parameter using **&lt;ParameterTypes&gt;** tags. In the above example, you explicitly specify that parameter "Size" is of "Int32" type and Parameter "Color" is a string. To summarize: **The ParameterTypes section is optional. By default, if parameter type information is not provided, it will be saved as a string.**

If you compare the Managed and Native examples, you will notice that the only difference between the two is the **&lt;ParameterTypes&gt;** block. The native XML file specifies Size to be of the native integer type "int" and uses the default type WEX::Common::String to be the type for Color by not specifying it. For your convenience, the following example shows the XML file from the native example.

```cpp
    1  <?xml version="1.0"?>
    2  <Data>
    3    <Table Id="SimpleTable">
    4      <ParameterTypes>
    5        <ParameterType Name="Size">int</ParameterType>
    6      </ParameterTypes>
    7      <Row>
    8        <Parameter Name="Size">4</Parameter>
    9        <Parameter Name="Color">White</Parameter>
    10     </Row>
    11     <Row>
    12       <Parameter Name="Size">10</Parameter>
    13       <Parameter Name="Color">Black</Parameter>
    14     </Row>
    15     <Row>
    16       <Parameter Name="Size">9</Parameter>
    17       <Parameter Name="Color">Orange</Parameter>
    18     </Row>
    19     <Row>
    20       <Parameter Name="Size">9</Parameter>
    21       <Parameter Name="Color">Blue</Parameter>
    22     </Row>
    23   </Table>
    24 </Data>
```

The parameter types supported in **Native** and **Managed** code, are listed [here](parameter-types-in-table-data-sources.md).

If any other data type is specified, the test will throw a warning and consider it to be a String.

Continuing back with the XML files, after the &lt;ParameterTypes&gt; block in both the XML files, you have identical set of **&lt;Row&gt;s**, which each correspond to one set of data in both our managed and native examples. In this particular case, you have 4 sets of Data defined by way of 4 &lt;Row&gt; blocks, each specifying the values of the parameters using the **&lt;Parameter&gt;** tags.

That covers the essential basics of the various parts of the data source file. Now let's see how you can retrieve the values that you specified in the above XML file.

## <span id="Authoring_test_to_be_a_data_driven_test"></span><span id="authoring_test_to_be_a_data_driven_test"></span><span id="AUTHORING_TEST_TO_BE_A_DATA_DRIVEN_TEST"></span>Authoring test to be a data driven test


Now that the data is specified, you need a way to associate the code or test method that will consume the data with this data in XML file. You do this - in both the managed and native examples - by specifying the **"DataSource"** metadata. The DataSource metadata has three parts to it:

1.  'Table:' - this identifies the data source as being an XML table.
2.  'DataDrivenTests.xml' - this is the file that contains the XML table.
3.  '\#Table2' - Following the '\#' delimeter, the 'Table2' value identifies the particular table within the XML document to use. A single XML Table data source can contain multiple tables. TAEF will look through the XML file for a Table element with an 'Id' attribute that matches the specified value.

Once again, lets take a quick look at the code that covers the above aspects.

### <span id="Native_code"></span><span id="native_code"></span><span id="NATIVE_CODE"></span>Native code

```cpp
1   class SimpleDataDrivenExample
2   {
3      BEGIN_TEST_CLASS(SimpleDataDrivenExample)
4        TEST_CLASS_PROPERTY(L"Description", L"Simple example in table-based data-driven tests")
5      END_TEST_CLASS()
6   
7      TEST_METHOD_CLEANUP(TestCleanup);
8      TEST_METHOD_SETUP(TestSetup);
9    
10     BEGIN_TEST_METHOD(DataDrivenTest)
11       TEST_METHOD_PROPERTY(L"DataSource", L"Table:SimpleDataDrivenExample.xml#SimpleTable")
11     END_TEST_METHOD()
12     ...
```

### <span id="Managed_code"></span><span id="managed_code"></span><span id="MANAGED_CODE"></span>Managed code

```cpp
    1 [TestMethod]
    2 [DataSource("Table:CSharpDataDrivenSimpleExample.xml#SimpleTable")]
    3 public void DataDrivenTest()
    4 {
    5  ...
    6 }
```

"DataSource" is a known property in Microsoft.VisualStudio.TestTools.UnitTesting.

In addition to the above, you need some extra steps for data driven tests in managed code. You also need to define a private TestContext property - like VSTS recommends (<https://msdn2.microsoft.com/library/ms404699(VS.80).aspx>). You also define public assessors to this property. Internally TAEF sets this TestContext property so you can access the data through it. Lets take a quick look at this portion of code:

```cpp
    1 public TestContext TestContext
    2 {
    3     get;
    4     set;
    5 }
```

## <span id="Retrieving_data_in_the_Test_method"></span><span id="retrieving_data_in_the_test_method"></span><span id="RETRIEVING_DATA_IN_THE_TEST_METHOD"></span>Retrieving data in the Test method


The retrieval APIs are different in managed and native code. Let's start with understanding the **native retrieval API**:

```cpp
    1  void SimpleDataDrivenExample::DataDrivenTest()
    2  {
    3          int size;
    4          if (SUCCEEDED(TestData::TryGetValue(L"size", size)))
    5          {
    6              VERIFY_ARE_NOT_EQUAL(size, 0);
    7              Log::Comment(String().Format(L"Size retrieved was %d", size));
    8          }
    9
    10         String color;
    11         if (SUCCEEDED(TestData::TryGetValue(L"color", color)))
    12         {
    13             Log::Comment(L"Size retrieved was " + color);
    14         }
    15
    16         unsigned int index;
    17         if (SUCCEEDED(TestData::TryGetValue(L"index", index)))
    18         {
    19             Log::Comment(String().Format(L"At index %d", index));
    20         }
    21 }
```

Pay special attention to lines 4, 11, and 17. Prior to each of these lines, define a local variable to save the data that you will retrieve. It is important to get the type right here. Since you defined "Size" to be an "int" type in the XML file, you must define a local variable of type int to retrieve it to. The retrieval API takes the name of the parameter to retrieve as a String value as its first parameter. The second parameter is the local variable passed in by reference and set by TAEF code.

This retrieval API is defined in **TestData.h** and included by the WexTestClass.h header that all TAEF tests include.

To retrieve the data in **managed code**, make use of the TestContext property that you defined. Take a look at the code below (or in example):

```cpp
    1  public void DataDrivenTest()
    2  {
    3     int size = (int)m_testContext.DataRow["Size"];
    4     Verify.AreNotEqual(size, 0);
    5     Log.Comment("Size is " + size.ToString());
    6
    7     Log.Comment("Color is " + m_testContext.DataRow["Color"]);
    8     UInt32 index = (UInt32)m_testContext.DataRow["Index"];
    9     Log.Comment("At index " + index.ToString());
    10 }
```

If you are familiar with VSTS, you will find that the example above is similar. Use the DataRow and specify the column name as the name of the parameter you are trying to retrieve.

If you look in the example, there is also a non data driven test in the same class. In other words, **you have the flexibility of combining DataDriven and NonDataDriven tests in the same test class.**

## <span id="Running_SimpleDataDrivenExample_with_TAEF"></span><span id="running_simpledatadrivenexample_with_taef"></span><span id="RUNNING_SIMPLEDATADRIVENEXAMPLE_WITH_TAEF"></span>Running SimpleDataDrivenExample with TAEF


Make sure you are aware of how to **Author Data Driven Tests** and how to **Execute Tests with TAEF** before you start with tips and tricks of executing DataDrivenTests with TAEF. It might be helpful to refresh your memory on how **Selection** works with TAEF.

The command prompt for executing data-driven tests is not very different from executing any generic test with TAEF. To run both examples (native and managed) that are described above, just run the following command:

<span id="TE.exe_Examples_CPP.DataDriven.Example.dll_Examples_CSharp.DataDriven.Example.dll__________________________name__Simple_"></span><span id="te.exe_examples_cpp.datadriven.example.dll_examples_csharp.datadriven.example.dll__________________________name__simple_"></span><span id="TE.EXE_EXAMPLES_CPP.DATADRIVEN.EXAMPLE.DLL_EXAMPLES_CSHARP.DATADRIVEN.EXAMPLE.DLL__________________________NAME__SIMPLE_"></span>TE.exe Examples\\CPP.DataDriven.Example.dll Examples\\CSharp.DataDriven.Example.dll /name:\*Simple\*  

The '/name' adds a selection criteria based on name and chooses only the classes that you are interested in. To select which tests to execute from within the classes, you should first list all of the properties of the dll. Then, you can decide which properties to use for selection criteria.

``` syntax
TE.exe Examples\CPP.DataDriven.Example.dll Examples\CSharp.DataDriven.Example.dll /name:*Simple* /listproperties
f:\Examples\CPP.DataDriven.Example.dll
        WEX::TestExecution::Examples::SimpleDataDrivenExample
                Property[Description] = Simple example in table-based data-driven tests

            WEX::TestExecution::Examples::SimpleDataDrivenExample::DataDrivenTest#0
                    Setup: TestSetup
                    Teardown: TestCleanup
                    Property[DataSource] = Table:SimpleDataDrivenExample.xml#SimpleTable

                    Data[Color] = White
                    Data[Size] = 4

            WEX::TestExecution::Examples::SimpleDataDrivenExample::DataDrivenTest#1
                    Setup: TestSetup
                    Teardown: TestCleanup
                    Property[DataSource] = Table:SimpleDataDrivenExample.xml#SimpleTable

                    Data[Color] = Black
                    Data[Size] = 10

            WEX::TestExecution::Examples::SimpleDataDrivenExample::DataDrivenTest#2
                    Setup: TestSetup
                    Teardown: TestCleanup
                    Property[DataSource] = Table:SimpleDataDrivenExample.xml#SimpleTable

                    Data[Color] = Orange
                    Data[Size] = 9

            WEX::TestExecution::Examples::SimpleDataDrivenExample::DataDrivenTest#3
                    Setup: TestSetup
                    Teardown: TestCleanup
                    Property[DataSource] = Table:SimpleDataDrivenExample.xml#SimpleTable

                    Data[Color] = Blue
                    Data[Size] = 9

            WEX::TestExecution::Examples::SimpleDataDrivenExample::FirstNonDataDrivenTest
                    Setup: TestSetup
                    Teardown: TestCleanup

            WEX::TestExecution::Examples::SimpleDataDrivenExample::SetsOfDataTest#metadataSet0
                    Setup: TestSetup
                    Teardown: TestCleanup
                    Property[Data:Color] = {Purple, Maroon, Brown}

                    Data[Color] = Purple

            WEX::TestExecution::Examples::SimpleDataDrivenExample::SetsOfDataTest#metadataSet1
                    Setup: TestSetup
                    Teardown: TestCleanup
                    Property[Data:Color] = {Purple, Maroon, Brown}

                    Data[Color] = Maroon

            WEX::TestExecution::Examples::SimpleDataDrivenExample::SetsOfDataTest#metadataSet2
                    Setup: TestSetup
                    Teardown: TestCleanup
                    Property[Data:Color] = {Purple, Maroon, Brown}

                    Data[Color] = Brown

            WEX::TestExecution::Examples::SimpleDataDrivenExample::SecondNonDataDrivenTest
                    Setup: TestSetup
                    Teardown: TestCleanup


        f:\Examples\CSharp.DataDriven.Example.dll
        WEX.Examples.CSharpDataDrivenSimpleExample
                Setup: MyClassInitialize
                Property[Description] = Simple example in table-based data-driven tests

            WEX.Examples.CSharpDataDrivenSimpleExample.DataDrivenTest#0
                    Property[DataSource] = Table:CSharpDataDrivenSimpleExample.xml#SimpleTable

                    Data[Color] = White
                    Data[Size] = 4

            WEX.Examples.CSharpDataDrivenSimpleExample.DataDrivenTest#1
                    Property[DataSource] = Table:CSharpDataDrivenSimpleExample.xml#SimpleTable

                    Data[Color] = Black
                    Data[Size] = 10

            WEX.Examples.CSharpDataDrivenSimpleExample.DataDrivenTest#2
                    Property[DataSource] = Table:CSharpDataDrivenSimpleExample.xml#SimpleTable

                    Data[Color] = Orange
                    Data[Size] = 9

            WEX.Examples.CSharpDataDrivenSimpleExample.DataDrivenTest#3
                    Property[DataSource] = Table:CSharpDataDrivenSimpleExample.xml#SimpleTable

                    Data[Color] = Blue
                    Data[Size] = 9

            WEX.Examples.CSharpDataDrivenSimpleExample.NonDataDrivenTest
            WEX.Examples.CSharpDataDrivenSimpleExample.SetsOfMetadataTest#metadataSet0
                    Property[Data:Color] = {Red, Green, Blue}

                    Data[Color] = Red

            WEX.Examples.CSharpDataDrivenSimpleExample.SetsOfMetadataTest#metadataSet1
                    Property[Data:Color] = {Red, Green, Blue}

                    Data[Color] = Green

            WEX.Examples.CSharpDataDrivenSimpleExample.SetsOfMetadataTest#metadataSet2
                    Property[Data:Color] = {Red, Green, Blue}

                    Data[Color] = Blue

```

For now, let's ignore the SetsOfMetadataTest and SetsOfDataTest listed above. If you are curious about these, read more on [Light-weight data-driven testing](light-weight-data-driven-testing.md). Now that you know the various properties and Data parameter name and values, you can select specific tests based on that. Try them out and follow along to confirm what you select.

To run only the non data-driven tests, run:

<span id="TE.exe_Examples_CSharp.DataDriven.Example.dll_Examples_CPP.DataDriven.Example.dll__________________________select___Name___Simple___And_not__DataSource____"></span><span id="te.exe_examples_csharp.datadriven.example.dll_examples_cpp.datadriven.example.dll__________________________select___name___simple___and_not__datasource____"></span><span id="TE.EXE_EXAMPLES_CSHARP.DATADRIVEN.EXAMPLE.DLL_EXAMPLES_CPP.DATADRIVEN.EXAMPLE.DLL__________________________SELECT___NAME___SIMPLE___AND_NOT__DATASOURCE____"></span>TE.exe Examples\\CSharp.DataDriven.Example.dll Examples\\CPP.DataDriven.Example.dll /select:"@Name='\*Simple\*' And not(@DataSource=\*)"  

Now, to run only those data driven tests, where color is specified as "Black", run:

<span id="TE.exe_Examples_CSharp.DataDriven.Example.dll_Examples_CPP.DataDriven.Example.dll__________________________select___Name___Simple___And__Data_Color__Black__"></span><span id="te.exe_examples_csharp.datadriven.example.dll_examples_cpp.datadriven.example.dll__________________________select___name___simple___and__data_color__black__"></span><span id="TE.EXE_EXAMPLES_CSHARP.DATADRIVEN.EXAMPLE.DLL_EXAMPLES_CPP.DATADRIVEN.EXAMPLE.DLL__________________________SELECT___NAME___SIMPLE___AND__DATA_COLOR__BLACK__"></span>TE.exe Examples\\CSharp.DataDriven.Example.dll Examples\\CPP.DataDriven.Example.dll /select:"@Name='\*Simple\*' And @Data:Color='Black'"  

Just like you did with "Color", <strong>@Data:&lt;DataDrivenParameterName&gt;=&lt;DataDrivenParameterValue&gt;</strong> will run specific data based on the DataDriven parameter value specified. In the above case, it will run WEX::TestExecution::Examples::SimpleDataDrivenExample::DataDrivenTest\#1 and WEX.Examples.CSharpDataDrivenSimpleExample.DataDrivenTest\#1

Notice the **test indices** in the listproperties above. You can select the above based on the index as well.

<span id="TE.exe_Examples_CSharp.DataDriven.Example.dll_Examples_CPP.DataDriven.Example.dll__________________________select___Name___Simple___And__Data_Index_1_"></span><span id="te.exe_examples_csharp.datadriven.example.dll_examples_cpp.datadriven.example.dll__________________________select___name___simple___and__data_index_1_"></span><span id="TE.EXE_EXAMPLES_CSHARP.DATADRIVEN.EXAMPLE.DLL_EXAMPLES_CPP.DATADRIVEN.EXAMPLE.DLL__________________________SELECT___NAME___SIMPLE___AND__DATA_INDEX_1_"></span>TE.exe Examples\\CSharp.DataDriven.Example.dll Examples\\CPP.DataDriven.Example.dll /select:"@Name='\*Simple\*' And @Data:Index=1"  

The above will run the same two tests that @Data:Color='Black' selected. You even add guards to the index selection with **@Data:Index &gt; lowerGuardValue and @Data:index &lt; upperGuardValue**

If you understand the basics of data driven testing with TAEF, follow along with the next class in the same examples: [Overriding metadata at the Row level](metadata-overriding-data-driven-test-example.md), [Specifying array parameter types](array-support-data-driven-test-example.md).









