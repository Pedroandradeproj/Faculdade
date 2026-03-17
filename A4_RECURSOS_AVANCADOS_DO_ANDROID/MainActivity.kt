package com.example.gestosesensoresapp

import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import android.os.Bundle
import android.view.GestureDetector
import android.view.MotionEvent
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {

    private lateinit var gestureDetector: GestureDetector
    private lateinit var sensorManager: SensorManager
    private var accelerometer: Sensor? = null

    private lateinit var tvGesto: TextView
    private lateinit var tvX: TextView
    private lateinit var tvY: TextView
    private lateinit var tvZ: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        // Ajusta padding para barras do sistema
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        // Inicializa TextViews
        tvGesto = findViewById(R.id.tvGesto)
        tvX = findViewById(R.id.tvX)
        tvY = findViewById(R.id.tvY)
        tvZ = findViewById(R.id.tvZ)

        // Inicializa GestureDetector
        val gestureListener = object : GestureDetector.SimpleOnGestureListener() {

            override fun onSingleTapConfirmed(e: MotionEvent): Boolean {
                tvGesto.text = "Toque simples detectado"
                return true
            }

            override fun onDoubleTap(e: MotionEvent): Boolean {
                tvGesto.text = "Duplo toque detectado"
                return true
            }

            override fun onLongPress(e: MotionEvent) {
                tvGesto.text = "Toque longo detectado"
            }

            override fun onFling(
                e1: MotionEvent?,  // primeiro evento pode ser nulo
                e2: MotionEvent,   // segundo evento NÃO pode ser nulo
                velocityX: Float,
                velocityY: Float
            ): Boolean {
                tvGesto.text = "Deslizar detectado"
                return true
            }
        }

        gestureDetector = GestureDetector(this, gestureListener)
        gestureDetector.setOnDoubleTapListener(gestureListener)

        // Inicializa o sensor acelerômetro
        sensorManager = getSystemService(SENSOR_SERVICE) as SensorManager
        accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
        accelerometer?.also { accel ->
            sensorManager.registerListener(sensorListener, accel, SensorManager.SENSOR_DELAY_NORMAL)
        }
    }

    // Repassa eventos de toque para o GestureDetector
    override fun onTouchEvent(event: MotionEvent): Boolean {
        gestureDetector.onTouchEvent(event)
        return super.onTouchEvent(event)
    }

    // Listener do acelerômetro
    private val sensorListener = object : SensorEventListener {
        override fun onSensorChanged(event: SensorEvent) {
            tvX.text = "X: ${event.values[0]}"
            tvY.text = "Y: ${event.values[1]}"
            tvZ.text = "Z: ${event.values[2]}"
        }

        override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {}
    }

    override fun onDestroy() {
        super.onDestroy()
        // Para de escutar o sensor quando Activity for destruída
        sensorManager.unregisterListener(sensorListener)
    }
}