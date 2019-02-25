---
title: Array Support Data Driven Test Example
description: Array Support Data Driven Test Example
ms.assetid: ECCDE395-C887-4485-8C8F-312EFCFD16A2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Array Support Data Driven Test Example


This section covers some advanced features of data driven testing by way of example. If you are still covering the basics, you might want to start with a [Simple Data Driven Example](data-driven-testing.md).

Examples referenced:

-   ArraySupportDataDrivenExample

-   CSharpDataDrivenArraySupportExample

Previous sections have already covered the basics of data driven test authoring and execution. The following list discusses the meaning of **Arrays** in the TAEF Data Driven Testing sense:

-   **Arrays are variable length, homogeneous type set of elements that are treated as a single parameter.**
-   **To specify an array type, you need to explicitly specify the type of the parameter in the ParameterTypes block and add an Array="true" attribute.**

The parameter types that are supported are listed [here](parameter-types-in-table-data-sources.md).

If any other data type is specified, the test throws a warning and considers it to be a String. In the case of arrays, the data type would be considered to be of type String\[\].

The following example shows how to specify that the parameter is an array of one of the basic types. It is important to note that there are no default types allowed in the case of arrays - you must explictly specify the type and set the **Array** attribute for the parameter to be true.

```cpp
1  <?xml version="1.0"?>
2  <Data>
3    <Table Id="ArraySupportTable">
4      <ParameterTypes>
5        <ParameterType Name="Size" Array="true">int</ParameterType>
6        <ParameterType Name="Color" Array="true">String</ParameterType>
7      </ParameterTypes>
8      <Row>
9        <Parameter Name="Size">4</Parameter>
10       <Parameter Name="Color">White</Parameter>
11     </Row>
12     <Row>
13       <Parameter Name="Size">
14         <Value>4</Value>
15         <Value>6</Value>
16         <Value>8</Value>
17       </Parameter>
18       <Parameter Name="Color">
19         <Value>Red</Value>
20         <Value>Green</Value>
21         <Value>Blue</Value>
22       </Parameter>
23     </Row>
24     <Row>
25       <Parameter Name="Size">
26         <Value>9</Value>
27         <Value>12</Value>
28         <Value>16</Value>
29       </Parameter>
30       <Parameter Name="Color">Orange</Parameter>
31     </Row>
32     <Row>
33       <Parameter Name="Size">9</Parameter>
34       <Parameter Name="Color">
35         <Value>White</Value>
36         <Value>Black</Value>
37       </Parameter>
38     </Row>
39   </Table>
40 </Data>
```

Examine the **Value** tags and the **Array** attributes in the example above. First, you must explicitly specify the type for both the **Size** and **Color** parameters and specify that these parameters are arrays, by setting the **Array** attribute to **true**. Then you specify the values in **&lt;Value&gt;...&lt;/Value&gt;** tags. You can have as many &lt;Value&gt; tags as you need to specify any number of values within the array for a given Row's parameter.

Notice lines 9, 10, 30, and 33 in the XML examples above. These entries are single valued array elements. In other words, **you may specify single valued array elements directly in the &lt;Parameter&gt; tag without an additional &lt;Value&gt; tag.** Also, **even though the parameter in the row has only one value, it is still treated as an array of one element and cannot be retrieved otherwise.**

Now, take a look at the retrieval APIs.

## <span id="Native_Retrieval"></span><span id="native_retrieval"></span><span id="NATIVE_RETRIEVAL"></span>Native Retrieval


Array elements can be retrieved in native code, by using the **WEX::TestExecution::TestDataArray&lt;&gt;** template class. See the published header TestData.h for details. The **TestDataArray** class manages the lifetime of the array elements and provides useful APIs to retrieve specific values within the array:

```cpp
1  namespace WEX { namespace TestExecution
2  {
3      template <typename T>
4      class TECOMMON_API TestDataArray sealed
5      {
6         ...
7      public:
8          TestDataArray();
9          ~TestDataArray();
10         const size_t GetSize() const;
11         T& operator[](size_t index);
12
13     private:
14        ...
15     };
16 } /* namespace TestExecution */ } /* namespace WEX */
```

You can obtain the length of the array by calling **GetSize** and can get a specific element by using the operator **\[\]**.

The next example shows how to use these functions in the code. Consider the cpp file in the native example:

```cpp
1  TestDataArray<int> sizes;
2  if (SUCCEEDED(TestData::TryGetValue(L"size", sizes)))
3  {
4      size_t count = sizes.GetSize();
5      for (size_t i = 0; i < count; ++i)
6      {
7          Log::Comment(String().Format(L"Size[%d] retrieved was %d", i, sizes[i]));
8      }
9  }
10
11 TestDataArray<String> colors;
12 if (SUCCEEDED(TestData::TryGetValue(L"color", colors)))
13 {
14     size_t count = colors.GetSize();
15     for (size_t i = 0; i < count; ++i)
16     {
17         Log::Comment(String().Format(L"Color[%d] retrieved was ", i) + colors[i]);
18     }
19 }
```

First, you define a local TestDataArray of the array type. In this case, **sizes** is an array of type int and **colors** is an array of type WEX::Common::String. The API to retrieve an Array is similar to the one that retrieves any variable. You call **TestData::TryGetValue**, ask it to retrieve the parameter **size**, and put the value into the local variable **sizes**.

**Note that an attempt to retrieve a non-array specified parameter into an array causes an error and fails the test. Similarly, an attempt to retrieve an array into a non-array variable, even if the array only has one element, causes an error.**

If an array parameter is not specified in the XML Row at all, an attempt to retrieve the parameter fails. For example, if a Row looked like:

```cpp
       <Row>
         <Parameter Name="Color">
           <Value>White</Value>
           <Value>Black</Value>
         </Parameter>
       </Row>
```

Notice that the parameter **Size**, which is an array, is not specified in the Row. If you attempt to retrieve **Size** from the code, the API call would return a failing return code. You could use this to define a default array value.

On the other hand, you can specify an empty array by specifying an empty parameter tag for **Size** as follows:

```cpp
       <Row>
         <Parameter Name="Size"></Parameter>
         <Parameter Name="Color">
           <Value>White</Value>
           <Value>Black</Value>
         </Parameter>
       </Row>
```

In this case, an attempt to retrieve **size** would succeed, but the array size would be 0.

## <span id="Managed_Retrieval"></span><span id="managed_retrieval"></span><span id="MANAGED_RETRIEVAL"></span>Managed Retrieval


Managed retrieval remains almost the same as before - only you need to make sure to retrieve the values into a local variable of the appropriate array type. Consider the following managed example:

```cpp
1  Int32[] sizes = m_testContext.DataRow["Size"] as Int32[];
2  foreach (int size in sizes)
3  {
4          Verify.AreNotEqual(size, 0);
5          Console.WriteLine("Size is " + size.ToString());
6  }
7
8  String[] colors = m_testContext.DataRow["Color"] as String[];
9  foreach (String color in colors)
10 {
11         Console.WriteLine("Color is " + color);
12 }
```

Similar to the native retrieval, if an array parameter is not specified in the XML Row at all, an attempt to retrieve the parameter returns an object of type **System.DBNull**. For example, if a Row looked like:

```cpp
       <Row>
         <Parameter Name="Color">
           <Value>White</Value>
           <Value>Black</Value>
         </Parameter>
       </Row>
```

Notice that the parameter **Size**, which is an array, is not specified in the Row. If you attempt to retrieve **Size** from the code, the API call would return an object of type **DBNull**. If you have any such values in your table, you may want to retrieve them from the context into an object first and take appropriate steps after comparing the type of object against **typeof(System.DBNull)** or the type that you are exepecting it to be.

On the other hand, you may specify an empty array by specifying an empty parameter tag for **Size** as follows:

```cpp
       <Row>
         <Parameter Name="Size"></Parameter>
         <Parameter Name="Color">
           <Value>White</Value>
           <Value>Black</Value>
         </Parameter>
       </Row>
```

In this case, an attempt to retrieve **size** succeessfully returns an empty array of type **System.Int32\[\]**.

## <span id="Execution"></span><span id="execution"></span><span id="EXECUTION"></span>Execution


Executing data driven tests that support arrays is no different from executing any other data driven test. The only key point of difference is that **the sematics of the selection criteria changes in the case of array data parameters to mean "contains" rather than "equals".**

To see what this means, assume that you want to select all data driven tests where the **Color** array contains the value **White**. To do this, run:

``` syntax
TE.exe Examples\CSharp.DataDriven.Example.dll /select:"@Name='*Array* And @Data:Color='White'"
```

``` syntax
TE.exe Examples\CPP.DataDriven.Example.dll /select:"@Name='*Array* And @Data:Color='White'"
```

This command runs the data driven tests with index \#0 and \#3 in both of the above cases.

You can build more complex queries which say, for example, select only the test in which the **color** array contains **white** and the **color** array contains **black**, which would only select data driven tests with index \#3. As an exercise, try writing and executing this query yourself.

 

 





