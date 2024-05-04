THESIS Associated with University of Thessaly

# USE OF DATA GROUPING ALGORITHMS FOR ANOMALY DETECTION IN IOT SYSTEMS

##  Implementation of Denstream clustering algorithm in an IoT device, to propose a low-cost approach to detect anomaly behavior in IoT.

In this thesis, an anomaly detection system is proposed that has as its main idea the use of a lightweight clustering algorithm in measurements related to the resource consumption of an IoT device. The purpose is to capture the current operation of the device in the clustering results of the algorithm, so that a profile of normal operation can be generated from them when the device is in a learning phase. Then, abnormal behavior may be detected whenever a new result of the algorithm clustering is not detected in the normal operation profile.
To examine the proposed system, an experimental procedure is followed in this paper in which :

    - A Raspberry Pi and Ubuntu Core software are chosen as the IoT environment that can be used to implement the proposed system.
    
    - A monitoring python snap application (psuitl-process-monitoring-snap) to capture device resource usage is created in this environment.
    
    - Normal and abnormal behaviours of the device is simulated in order to collect measurements corresponding to different operations.
        - For the simulation of the normal behavior we created flasktemp, a weather python snap application using flask wewb framework.
        - For the simulation of the abnormal behavior we created pyflooder-flasktemp, an HTTP Flood Python snap that could stop the webpage used in 'flasktemp'.
        
    - DenStream is chosen as the algorithm for clustering the measurements. DenStream, was chosen as it uses a pioneering mechanism to detect groups in a stream, by which it keeps in memory specific points. Unlike other clustering algorithms, it aims for an approximate result, and focuses on lightweight clustering.
    
    - The efficiency of DenStream in each behavioral simulation is examined. 
      
If in the results of the non-normal behavior simulation, the existence of an additional behavior is detected in a lightweight way, then it means that in a time interval where the device performs its normal operation, a normal operation profile can be generated (by storing the results of the algorithm clustering). Then the abnormal behaviour can be detected when the results of a new clustering are not detected in the normal operation profile.

