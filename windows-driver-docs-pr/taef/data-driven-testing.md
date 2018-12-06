---
title: Data Driven Testing
description: Data Driven Testing
ms.assetid: 409CC5FD-1632-4120-95C6-60574C9BAD32
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Driven Testing


Data-driven Testing is a testing methodology where a Test's input and output values are separated from the code. This formalism typically means that a small investment in making the test code a little bit more generic allows for a large number of test cases to be written by simply identifying the data that's involved.

Data Driven Testing is great for testing areas that work with a set of input values that define their behavior - for example, when testing an API, the input and output parameters can be defined as a source of data, and the test code consumes the data, makes the API calls and validates the results.

## <span id="Data-driven_Testing_support_in_TAEF"></span><span id="data-driven_testing_support_in_taef"></span><span id="DATA-DRIVEN_TESTING_SUPPORT_IN_TAEF"></span>Data-driven Testing support in TAEF


TAEF offers a variety of options for authoring data-driven tests. Let's understand these options so you can choose which one fits your test scenario best.

**Table based data-driven testing** solution allows you fine grained controlled on the data parameter variations as well as defining the parameter types. The DataSource in this case is a table defined in an XML file. You can specify the parameter types(int, unsigned int, size\_t, bool, double, DWORD, \_\_int64 etc and their homogeneous array variant), or have the type default to WEX::Common::String (native) or string (managed). Each Row in the table is a set of variation on the parameter values. The test method will be re-invoked for every Row in the table. Here is a snippet of an XML DataSource for table based data-driven testing:

```cpp
1  <?xml version="1.0"?>
2   <Data>
3     <Table Id ="Table1">
4          <ParameterTypes>
5                  <ParameterType Name="Size">Int32</ParameterType>
6                  <ParameterType Name="Color">String</ParameterType>
7          </ParameterTypes>
8          <Row>
9                 <Parameter Name="Size">12</Parameter>
10                 <Parameter Name="Color">Blue</Parameter>
11         </Row>
12         <Row>
13                 <Parameter Name="Size">4</Parameter>
14                 <Parameter Name="Color">White</Parameter>
15         </Row>
16         <Row>
17                 <Parameter Name="Size">9</Parameter>
18                 <Parameter Name="Color">Black</Parameter>
19         </Row>
20    </Table>
21  </Data>
```

To read more: [Table based data-driven testing](table-data-source.md).

The **Light-weight data-driven testing** support doesn't provide the full fidelity that Table based data-driven testing solution offers. To clarify: Light weight data-driven testing restricts data parameters to be WEX::Common::String(native) or String(managed) as against the various types supported by the Table based data-driven testing solution. But if you are looking for a low-cost and quick data variation (of say one or two parameters) to make a test method data-driven, and adding an XML file as the DataSource appears to be not worth the trouble, Light-weight data-driven testing could be exactly what you are looking for. A great example of this is a developer writing a unit test for an API say OpenThemeData(...) and wants to verify the API against "Button", "Listbox" and "ScrollBar". It might be too much of an overload to create an XML DataSource file for this, but with light-weight data-driven testing support this could be done efficiently in the source code itself. If more than one parameter is specified, TAEF will generate an n-way combinatorial expansion of parameters behind the scene and the test method will be invoked for each combination. To read more: [Light-weight data-driven testing](light-weight-data-driven-testing.md).

The n-way combinatorial expansion that light weight data-driven testing offers, could get expensive and provide diminishing returns as the test scenario gets more complex. In such complex test scenario, Pairwise Independent Combinatorial Testing(PICT) offered by **PICT based Data-driven testing** solution may be what you are looking for. PICT provides a lot of value by generating a compact set of parameter results to get comprehensive coverage over the parameters. Find out links to learn more about PICT and how to use this solution on [PICT based data-driven testing](pict-data-source.md) solution.

Using the **WMI based data-driven testing** support, you can also add precondition to your tests as well as obtain information (data) based upon the resources available on the test machine. For example, if you want to run the test only if the machine is domain joined and you also need the domain name information when you run the test. The DataSource in this case is a WQL query. Learn more about how to leverage [WMI Based data-driven testing](wmi-data-source.md) in your test scenario.

Being mindful of all the options listed above, you may also come up with a design where a combination of the above options may seem fit. For example, you may want to use a WMI query to get information about all the printers connected to the test machine, but there could be another set of parameters which can be defined upfront using a table based data-driven testing construct. **Multiple DataSource** specification may also be useful, if you want your test's data to come from two separate tables, hence allowing each table to be re-usable across other tests. Read the details on how to specify multiple DataSources for a test and what constraints apply while doing so: [Specifying Multiple DataSources](multiple-datasources.md)

## <span id="in_this_section"></span>In this section


-   [Data-driven Testing in Scripting Languages](data-driven-testing-in-scripting-languages.md)
-   [Table Data Source](table-data-source.md)
-   [Parameter Types in Table Data Sources](parameter-types-in-table-data-sources.md)
-   [Simple Data Driven Test Example](simple-data-driven-test-example.md)
-   [Metadata Overriding Data Driven Test Example](metadata-overriding-data-driven-test-example.md)
-   [Array Support Data Driven Test Example](array-support-data-driven-test-example.md)
-   [Data-driven Class](data-driven-class.md)
-   [PICT Data Source](pict-data-source.md)
-   [WMI Data Source](wmi-data-source.md)
-   [Light-weight Data-driven Testing](light-weight-data-driven-testing.md)
-   [Executing Data-driven tests](executing-data-driven-tests.md)
-   [Multiple DataSources](multiple-datasources.md)

 

 





