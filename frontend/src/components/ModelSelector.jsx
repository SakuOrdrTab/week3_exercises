/* eslint-disable react/prop-types */

const ModelSelector = ({ model, setModel }) => {
    return (
        <select
        value={model}
        onChange={(e) => setModel(e.target.value)}
        style={{ width: '100%', padding: '5px', marginBottom: '10px' }}
      >
        <option value="custom">Custom Model</option>
        <option value="llama">Llama 3</option>
      </select>
    )
}

export default ModelSelector