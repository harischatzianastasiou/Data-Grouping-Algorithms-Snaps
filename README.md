THESIS Associated with University of Thessaly

# USE OF DATA GROUPING ALGORITHMS FOR ANOMALY DETECTION IN IOT SYSTEMS

<p>  IoT devices are used in a multitude of applications that extend their influence across many sectors and activities. With the increasing rate of application of these devices, their success lies in their ability to be secured. Most of the IoT devices have limited computing resources. Therefore, the classical security mechanisms applied to most information systems cannot be applied to them. In this thesis, we consider the use of a lightweight clustering algorithm (DenStream), on measurements concerning the resource consumption of an IoT device, with the aim of capturing a change in the behavior of the device from the clustered results. The proposed system involves, the creation of a suitable IoT environment, using Ubuntu Core software. In this environment, snap applications are implemented in order to simulate a normal and abnormal operation of the device, and to collect measurements for each simulated operation. DenStream is evaluated with these metrics, taking into account the ability to create successful clusters, but also the workload on the device resources. </p>


#### Experimental procedure to examine the proposed system

    - A Raspberry Pi and Ubuntu Core software are chosen as the IoT environment that can be used to implement the proposed system.
    
    - A monitoring python snap application is created ([psuitl-process-monitoring-snap][1]), in order to capture device resource usage. 
    
    - Normal and abnormal behaviour of the device is simulated to collect measurements corresponding to different operations.
        - For the simulation of the normal behavior we created [flasktemp][2] and mystartup-snap. Flasktemp is a weather python snap application using flask web framework. Mystartup-snap is a snap bash script, to automatically run the weather python snap application when the device starts.
        - For the simulation of the abnormal behavior we created [pyflooder-flasktemp][3], an HTTP Flood python script that could stop the webpage used in 'flasktemp'.
        
    - [DenStream][4] is chosen as the algorithm for clustering the measurements. DenStream, was chosen as it uses a pioneering mechanism to detect groups in a stream, by which it keeps in memory specific points. Unlike other clustering algorithms, it aims for an approximate result, and focuses on lightweight clustering.
    
    - The efficiency of DenStream in each behavioral simulation is examined.
    
    - Other clustering algorithms are examined, to identify if DenStream outperforms them.
      
If anomalies are detected in the results of the abnormal behavior simulation, indicating the presence of additional behavior in a subtle manner, it implies that over a period during which the device conducts its regular operations, a profile of normal behavior can be established (by storing the outcomes of the algorithm's clustering). Subsequently, abnormal behavior can be identified when the results of a new clustering fail to align with the established profile of normal operation.

<p> [1] (https://snapcraft.io/psutil-process-monitoring-snap)
[2] (https://snapcraft.io/flasktemp)
[3] (https://snapcraft.io/pyflooder-flasktemp)
[4] Cao, Feng, Martin Estert, Weining Qian, and Aoying Zhou. "Density-based clustering over an evolving data stream with noise." In Proceedings of the 2006 SIAM international conference on data mining, pp. 328-339. Society for Industrial and Applied Mathematics, 2006. </p>

