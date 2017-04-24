---
title: Metadata Overriding Data Driven Test Example
description: Metadata Overriding Data Driven Test Example
ms.assetid: F39A556F-1816-4272-ABDE-62164AE09685
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Metadata Overriding Data Driven Test Example


This section covers some advanced features of data driven testing by way of example. If you are still covering the basics, you might want to start with a [Simple Data Driven Example.](simple-data-driven-test-example.md)

Examples referenced:

-   MetadataOverridingDataDrivenExample

-   DataDrivenMetadataOverridingExample

If you compare the examples that are covered on this section to the ones that are covered in the [Simple Data Driven Example](simple-data-driven-test-example.md) page, you will notice that the only difference is that metadata and properties at various levels in the test have been added. Lets first look at how a basic test is authored.

In the native example, observe lines 5 and 10 in the code example below:

```
1   class MetadataOverridingDataDrivenExample
2   {
3      BEGIN_TEST_CLASS(MetadataOverridingDataDrivenExample)
4          ...
5          TEST_CLASS_PROPERTY(L"Priority", L"2")
6      END_TEST_CLASS()
7    
8      BEGIN_TEST_METHOD(DataDrivenTest)
9          ...
10     TEST_METHOD_PROPERTY(L"Owner", L"wex")
11     END_TEST_METHOD()
12  }
```

So all tests defined in Class "MetadataOverridingDataDrivenExample" has priority of 2. Remember, tests can override any metadata specified at a level above them (class or module). In this case, DataDrivenTest method still maintains the priority of 2 and has its "Owner" defined to be "WEX". Now if this were a non-data driven test, you could choose based on any of this, /select:"@Priority=2" or /select:"@Owner='WEX'", and execute the test method in it. But **with data driven tests, you can further override the property applicable at the test method level by specifying metadata at the "Row" level.**

Let's look at the XML file to understand how.

```
    1  <?xml version="1.0"?>
    2  <Data>
    3    <Table Id="MetadataTable">
    4      <ParameterTypes>
    5        <ParameterType Name="Size">int</ParameterType>
    6      </ParameterTypes>
    7      <Row Priority="1">
    8        <Parameter Name="Size">4</Parameter>
    9        <Parameter Name="Color">White</Parameter>
    10      </Row>
    11      <Row Owner="C2">
    12        <Parameter Name="Size">10</Parameter>
    13        <Parameter Name="Color">Black</Parameter>
    14      </Row>
    15      <Row Priority="1" Owner="C3">
    16        <Parameter Name="Size">9</Parameter>
    17        <Parameter Name="Color">Orange</Parameter>
    18      </Row>
    19      <Row>
    20        <Parameter Name="Size">9</Parameter>
    21        <Parameter Name="Color">Blue</Parameter>
    22      </Row>
    23    </Table>
    24  </Data>
```

In the first 3 rows, the example overrides some metadata by explicitly specifying the metadata for the particular set of data values. The last set of data however has the same metadata as the method that contains it: Priority=2 and Owner=WEX.

Let's take a look at the managed code before looking into the selection and execution of these tests.

```
1   [TestClass]
2   public class DataDrivenMetadataOverridingExample
3   {
4      [ClassInitialize]
5      [Priority(2)]
6      public static void MyClassInitialize(Object testContext)
7      {
8      }
9   
9      [TestMethod]
10     ...
11     [TestProperty("Owner", "WEX")]
12     public void DataDrivenTest()
13     {
14        ...
15     }
...
```

You are mimicking the properties in the native example exactly over here as well.

Now, let's understand the overriding a little better:

``` syntax
TE.exe Examples\CSharp.DataDriven.Example.dll /select:"@Name='*overriding*' and @Priority=1"
```

will run

-   WEX.Examples.DataDrivenMetadataOverridingExample.DataDrivenTest\#0
-   WEX.Examples.DataDrivenMetadataOverridingExample.DataDrivenTest\#2

``` syntax
TE.exe Examples\CPP.DataDriven.Example.dll /select:"@Name='*overriding*' and @Priority=1"
```

will run:

-   WEX::TestExecution::Examples::MetadataOverridingDataDrivenExample::DataDrivenTest\#0
-   WEX::TestExecution::Examples::MetadataOverridingDataDrivenExample::DataDrivenTest\#2

## <span id="Exercise_for_the_reader"></span><span id="exercise_for_the_reader"></span><span id="EXERCISE_FOR_THE_READER"></span>Exercise for the reader


As an exercise, try adding new metadata values. Only varying the selection criteria in the above examples,

``` syntax
/select:"@Name='*overriding*' and @Owner='WEX'"
```

will run data driven tests with index \#0 and \#3 in both managed and native examples

``` syntax
 /select:"@Name='*overriding*' and @Priority=2"
```

will run data driven tests with index \#1 and \#3 and also run the NonDataDrivenTest in the managed example

``` syntax
TE.exe Examples\CPP.DataDriven.Example.dll Examples\CSharp.DataDriven.Example.dll /name:*overriding* /listproperties
    F:\ Examples\CPP.DataDriven.Example.dll
        WEX::TestExecution::Examples::MetadataOverridingDataDrivenExample
                Property[Priority] = 2

            WEX::TestExecution::Examples::MetadataOverridingDataDrivenExample::DataDrivenTest#0
                    Property[Owner] = WEX
                    Property[Priority] = 1
                    Property[DataSource] =  Table:MetadataOverridingDataDrivenExample.xml#MetadataTable

                    Data[Color] = White
                    Data[Size] = 4

            WEX::TestExecution::Examples::MetadataOverridingDataDrivenExample::DataDrivenTest#1
                    Property[Owner] = C2
                    Property[DataSource] =  Table:MetadataOverridingDataDrivenExample.xml#MetadataTable

                    Data[Color] = Black
                    Data[Size] = 10

            WEX::TestExecution::Examples::MetadataOverridingDataDrivenExample::DataDrivenTest#2
                    Property[Owner] = C3
                    Property[Priority] = 1
                    Property[DataSource] =  Table:MetadataOverridingDataDrivenExample.xml#MetadataTable

                    Data[Color] = Orange
                    Data[Size] = 9

            WEX::TestExecution::Examples::MetadataOverridingDataDrivenExample::DataDrivenTest#3
                    Property[Owner] = WEX
                    Property[DataSource] =  Table:MetadataOverridingDataDrivenExample.xml#MetadataTable

                    Data[Color] = Blue
                    Data[Size] = 9

    F:\ Examples\CSharp.DataDriven.Example.dll
        WEX.Examples.DataDrivenMetadataOverridingExample
                Setup: MyClassInitialize
                Property[Priority] = 2

            WEX.Examples.DataDrivenMetadataOverridingExample.DataDrivenTest#0
                    Property[DataSource] = Table:CSharpDataDrivenMetadataOverridingExample.xml#MetadataTable
                    Property[Owner] = WEX
                    Property[Priority] = 1

                    Data[Color] = White
                    Data[Size] = 4

            WEX.Examples.DataDrivenMetadataOverridingExample.DataDrivenTest#1
                    Property[DataSource] = Table:CSharpDataDrivenMetadataOverridingExample.xml#MetadataTable
                    Property[Owner] = C2

                    Data[Color] = Black
                    Data[Size] = 10

            WEX.Examples.DataDrivenMetadataOverridingExample.DataDrivenTest#2
                    Property[DataSource] = Table:CSharpDataDrivenMetadataOverridingExample.xml#MetadataTable
                    Property[Owner] = C3
                    Property[Priority] = 1

                    Data[Color] = Orange
                    Data[Size] = 9

            WEX.Examples.DataDrivenMetadataOverridingExample.DataDrivenTest#3
                    Property[DataSource] = Table:CSharpDataDrivenMetadataOverridingExample.xml#MetadataTable
                    Property[Owner] = WEX

                    Data[Color] = Blue
                    Data[Size] = 9

        WEX.Examples.DataDrivenMetadataOverridingExample.NonDataDrivenTest
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Metadata%20Overriding%20Data%20Driven%20Test%20Example%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




