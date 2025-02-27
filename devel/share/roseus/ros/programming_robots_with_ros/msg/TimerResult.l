;; Auto-generated. Do not edit!


(when (boundp 'programming_robots_with_ros::TimerResult)
  (if (not (find-package "PROGRAMMING_ROBOTS_WITH_ROS"))
    (make-package "PROGRAMMING_ROBOTS_WITH_ROS"))
  (shadow 'TimerResult (find-package "PROGRAMMING_ROBOTS_WITH_ROS")))
(unless (find-package "PROGRAMMING_ROBOTS_WITH_ROS::TIMERRESULT")
  (make-package "PROGRAMMING_ROBOTS_WITH_ROS::TIMERRESULT"))

(in-package "ROS")
;;//! \htmlinclude TimerResult.msg.html


(defclass programming_robots_with_ros::TimerResult
  :super ros::object
  :slots (_time_elapsed _updates_sent ))

(defmethod programming_robots_with_ros::TimerResult
  (:init
   (&key
    ((:time_elapsed __time_elapsed) (instance ros::time :init))
    ((:updates_sent __updates_sent) 0)
    )
   (send-super :init)
   (setq _time_elapsed __time_elapsed)
   (setq _updates_sent (round __updates_sent))
   self)
  (:time_elapsed
   (&optional __time_elapsed)
   (if __time_elapsed (setq _time_elapsed __time_elapsed)) _time_elapsed)
  (:updates_sent
   (&optional __updates_sent)
   (if __updates_sent (setq _updates_sent __updates_sent)) _updates_sent)
  (:serialization-length
   ()
   (+
    ;; duration _time_elapsed
    8
    ;; uint32 _updates_sent
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; duration _time_elapsed
       (write-long (send _time_elapsed :sec) s) (write-long (send _time_elapsed :nsec) s)
     ;; uint32 _updates_sent
       (write-long _updates_sent s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; duration _time_elapsed
     (send _time_elapsed :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _time_elapsed :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _updates_sent
     (setq _updates_sent (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get programming_robots_with_ros::TimerResult :md5sum-) "8227810e22df8077dd49231152c9e200")
(setf (get programming_robots_with_ros::TimerResult :datatype-) "programming_robots_with_ros/TimerResult")
(setf (get programming_robots_with_ros::TimerResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#result definition
duration time_elapsed
uint32 updates_sent

")



(provide :programming_robots_with_ros/TimerResult "8227810e22df8077dd49231152c9e200")


