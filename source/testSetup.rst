              
    **Document Number: TBD**


   **Document Revision History**

   +---------------+---------------------+---------------+---------------+
   | **Version**   |   **Comment**       |  **Author**   |    **Date**   |
   +---------------+---------------------+---------------+---------------+
   |  v1.0         |   Initial version   |   SnapRoute   |   10/22/2016  |
   +---------------+---------------------+---------------+---------------+
   |  v1.1         |  Revised test cases |   SnapRoute   |   10/25/2016  |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+


   **Document Approval History**

   +---------------+---------------------+---------------+---------------+
   | **Version**   |   **Comment**       |  **Author**   |    **Date**   |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
    
|   
|   
|   
|
|

==================
Voyager Test Setup
==================

    
|   
|   
|   

.. image:: VoyagerTestSetup.jpg


**Description**


  The diagram above depicts the Voyager testbed setup. The testbed utilizes a 40G switch as a traffic source.
  Voyager unit 1 and Voyager unit 2 have, AC400 module 0, NW interface id 0 connected to each other.

  Given the above topology, bidirectional traffic flows can be setup originating from port 49/50 on the traffic
  generator, switched by the Voyager units 1/2 and terminating at the traffic generator.

  The test setup also provides for running traffic loopback tests. Voyager unit 2 has network interfaces 0 and 1
  looped back on AC400 module 1.

  Additionally, Voyager unit 1 has only one AC400 module, while Voyager unit 2 is fully populated with 2 AC400
  modules. This provides for test coverage, ensuring full functionality is available even if only 1 AC400 module
  is present in the transponder system.

|   
|   
|   
|   
|   
|   
