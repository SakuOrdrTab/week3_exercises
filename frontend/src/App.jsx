import { useState } from 'react'
import postText from './services/sentiment-service'
import ReviewArea from './components/ReviewArea'
import ModelSelector from './components/ModelSelector'
import AnalyzeButton from './components/AnalyzeButton'

function App() {
  const [text, setText] = useState('')
  const [model, setModel] = useState('custom')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleAnalyze = async () => {
    // no empty texts
    if (!text.trim()) {
      alert('Please enter some text')
      return
    }

    setLoading(true)
    const response = await postText(text, model)
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

      <ReviewArea text={text} setText={setText} />
      <ModelSelector model={model} setModel={setModel} />
      <AnalyzeButton handleAnalyze={handleAnalyze} loading={loading} />

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
