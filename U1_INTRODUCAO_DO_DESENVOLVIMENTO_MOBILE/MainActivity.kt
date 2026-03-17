package com.example.cadastroapp

import android.os.Bundle
import android.widget.*
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val edtNome = findViewById<EditText>(R.id.edtNome)
        val edtEmail = findViewById<EditText>(R.id.edtEmail)
        val edtTelefone = findViewById<EditText>(R.id.edtTelefone)
        val edtSenha = findViewById<EditText>(R.id.edtSenha)

        val checkTermos = findViewById<CheckBox>(R.id.checkTermos)
        val btnEnviar = findViewById<Button>(R.id.btnEnviar)
        val txtAbrirTermos = findViewById<TextView>(R.id.txtAbrirTermos)

        btnEnviar.isEnabled = false

        checkTermos.setOnCheckedChangeListener { _, isChecked ->
            btnEnviar.isEnabled = isChecked
        }

        txtAbrirTermos.setOnClickListener {
            AlertDialog.Builder(this)
                .setTitle("Termos de Uso")
                .setMessage("""
                    Termos de Uso do Aplicativo
                    
                    1. Aceitação dos Termos
                    Ao utilizar este aplicativo, você concorda com os termos.
                    
                    2. Uso
                    Uso responsável e pessoal.
                    
                    3. Privacidade
                    Seus dados serão protegidos.
                    
                    4. Responsabilidade
                    Uso por sua conta e risco.
                """.trimIndent())
                .setPositiveButton("Fechar", null)
                .show()
        }

        btnEnviar.setOnClickListener {
            val nome = edtNome.text.toString()
            val email = edtEmail.text.toString()
            val telefone = edtTelefone.text.toString()
            val senha = edtSenha.text.toString()

            if (nome.isEmpty() || email.isEmpty() || telefone.isEmpty() || senha.isEmpty()) {
                Toast.makeText(this, "Preencha todos os campos", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            Toast.makeText(this, "Cadastro realizado com sucesso!", Toast.LENGTH_LONG).show()
        }
    }
}