THESIS Associated with University of Thessaly

# USE OF DATA GROUPING ALGORITHMS FOR ANOMALY DETECTION IN IOT SYSTEMS

<p>  IoT devices are used in a multitude of applications that extend their influence across many sectors and activities. With the increasing rate of application of these devices, their success lies in their ability to be secured. Most of the IoT devices have limited computing resources. Therefore, the classical security mechanisms applied to most information systems cannot be applied to them. In this thesis, we consider the use of a lightweight clustering algorithm on measurements concerning the resource consumption of an IoT device, with the aim of capturing a change in the behavior of the device from the clustered results. The proposed system involves, the creation of a suitable IoT environment, using Ubuntu Core software. In this environment, snap applications are implemented in order to simulate a normal and abnormal operation of the device, and to collect measurements for each simulated operation. The clustering algorithm is evaluated with these metrics, taking into account the ability to create successful clusters, but also the workload on the device resources. After the experimental proof of the proposed system, it is possible to construct an anomaly detection system by storing the clustered measurements describing the normal behavior of the device in a normal operation profile. </p>


<h3> Experimental procedure to examine the proposed system

    - A Raspberry Pi and Ubuntu Core software are chosen as the IoT environment that can be used to implement the proposed system.
    
    - A monitoring python snap application (psuitl-process-monitoring-snap) to capture device resource usage is created in this environment.
    
    - Normal and abnormal behaviours of the device is simulated in order to collect measurements corresponding to different operations.
        - For the simulation of the normal behavior we created flasktemp, a weather python snap application using flask wewb framework.
        - For the simulation of the abnormal behavior we created pyflooder-flasktemp, an HTTP Flood Python snap that could stop the webpage used in 'flasktemp'.
        
    - DenStream is chosen as the algorithm for clustering the measurements. DenStream, was chosen as it uses a pioneering mechanism to detect groups in a stream, by which it keeps in memory specific points. Unlike other clustering algorithms, it aims for an approximate result, and focuses on lightweight clustering.
    
    - The efficiency of DenStream in each behavioral simulation, compared to other clustering algorithms, is examined. 
      
If in the results of the non-normal behavior simulation, the existence of an additional behavior is detected in a lightweight way, then it means that in a time interval where the device performs its normal operation, a normal operation profile can be generated (by storing the results of the algorithm clustering). Then the abnormal behaviour can be detected when the results of a new clustering are not detected in the normal operation profile.

