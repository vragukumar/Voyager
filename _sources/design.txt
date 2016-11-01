.. FlexSwitchApis documentation master file, created by
   sphinx-quickstart on Mon Sep 26 18:29:20 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FlexSwitch API Documentation
============================

      **FlexSwitch offers the following :**
        - Fully programmable network protocol stack 
        - RESTful APIs at every level 
        - Highly customizable behavior
        - Works with select Optical Modules
        - Portable architecture to work on hardware from variety of vendors like Acton, Celestica, Alpha Networks, Facebook Wedge
        - Highly instrumented to help the Network operators troubleshoot issues

Who should read this document
-----------------------------
       This document is primarily intended for developers working in the areas like Network Management Systems (NMS), Element Management Systems (EMS). This document would also help any developer interested in developing creative applications.

       This document attempts to introduce you to **REST API** (REpresentational State Transfer) semantics in section :ref:`rest_primer`. Feel free to skip this secion if you are a REST ninja.
    
       FlexSwitch software model for REST APIs is described in :ref:`flex_api_model`. FlexSwitch objects a.k.a REST endpoints are described in  :ref:`flex_object_model`.


.. _rest_primer:

What is REST API any way
------------------------
       REST is a simple way to organize interactions between independent systems. REST model is not limited to a particular transportation, however HTTP/HTTPS is the most used form of transfer protocol for REST based systems. 
       REST design constitutes of resources (objects) and verbs (operations). The resources are generally designed to be independent. All resources support similar operations. Common operations supported by FlexSwitch software and their purpose is listed below

+----------------+--------------------------------+
|   Operation    |     Purpose                    |
+================+========+=======================+
| GET            |        Retrieve a object       |
+----------------+--------------------------------+
| POST           | Create an object               |
+----------------+--------------------------------+
| PATCH          | Update an existing object      |
+----------------+--------------------------------+
| DELETE         | Delete an existing object      |
+----------------+--------------------------------+


.. _flex_api_model:

FlexSwitch API Model
--------------------

       FlexSwitch partitions objects into config, state objects. These APIs allow users to configure or retrieve various objects. 
       All the config APIs are identified by the URL http://ipaddress/public/v<Version#>/config/<object>. 

       Similarly all the state objects are identified by the URL http://ipaddress/public/v<Version#>/state/<object>.

       In addition to these APIs FlexSwitch also supports retrieving of all autonomus events happened in the system with a URL at http://ipaddress/public/v1/events/Events/. 

       Similarly FlexSwitch provides Faults and Alarms.  The following sections describe complete object list in detail


.. _flex_object_model:

FlexSwitch Objects 
------------------
        FlexSwitch Objects are classified into config and state objects. Below link contains the list of model objects provided by FlexSwitch.

.. toctree::
   :maxdepth: 2

   Model Objects       <modelObjects>
