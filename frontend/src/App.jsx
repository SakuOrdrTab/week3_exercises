import { useState } from 'react'
import analyzeSentiment from './services/sentiment-service'

function App() {
  const [text, setText] = useState('')
  const [model, setModel] = useState('custom')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleAnalyze = async () => {
    if (!text.trim()) {
      alert('Please enter some text')
      return
    }

    setLoading(true)
    const response = await analyzeSentiment(text, model)
    setLoading(false)

    if (response.error) {
      setResult({ error: response.error })
    } else {
      setResult(response)
    }
  }

  return (
    <div style={{ maxWidth: '500px', margin: 'auto', textAlign: 'center', padding: '20px' }}>
      <h2>Sentiment Analyzer</h2>

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text here..."
        rows="4"
        style={{ width: '100%', marginBottom: '10px', padding: '5px' }}
      />

      <select
        value={model}
        onChange={(e) => setModel(e.target.value)}
        style={{ width: '100%', padding: '5px', marginBottom: '10px' }}
      >
        <option value="custom">Custom Model</option>
        <option value="llama">Llama 3</option>
      </select>

      <button onClick={handleAnalyze} disabled={loading} style={{ width: '100%', padding: '10px', fontWeight: 'bold' }}>
        {loading ? 'Analyzing...' : 'Analyze Sentiment'}
      </button>

      {result && (
        <div style={{ marginTop: '20px', padding: '10px', border: '1px solid #ccc', borderRadius: '5px' }}>
          {result.error ? (
            <p style={{ color: 'red' }}>{result.error}</p>
          ) : (
            <>
              <p><strong>Sentiment:</strong> {result.sentiment}</p>
              {result.confidence && <p><strong>Confidence:</strong> {result.confidence.toFixed(2)}</p>}
            </>
          )}
        </div>
      )}
    </div>
  )
}

export default App
